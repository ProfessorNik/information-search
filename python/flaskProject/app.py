from flask import Flask, render_template, redirect, request
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

login_manager = LoginManager()
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql+psycopg2://postgres:admin@localhost:5432/sample'
app.config['SECRET_KEY'] = '15430d2309e3866feec73d4c7008b61cf1c5675c'
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager.init_app(app)


class UserLogin:
    def __init__(self):
        self.__user = None

    def db_emerge(self, user_id):
        self.__user = User.query.filter_by(id=user_id).first()
        return self

    def emerge(self, user):
        self.__user = user
        return self

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user.id)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(30), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


class University(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    short_name = db.Column(db.String(100), nullable=False)
    foundation_date = db.Column(db.Date)


class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    birthday = db.Column(db.Date, nullable=False)
    university_id = db.Column(db.Integer, db.ForeignKey('university.id'), nullable=False)
    university = db.relationship('University', lazy=True)
    admission_year = db.Column(db.Integer, nullable=False)


@login_manager.user_loader
def user_loader(user_id):
    return UserLogin().db_emerge(user_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user is None:
            return render_template('auth/login.html', message='Некорректное имя пользователя')
        if user.password != password:
            return render_template('auth/login.html', message='Некорректный пароль')

        user_login = UserLogin().emerge(user)
        login_user(user_login)
        return redirect('/')

    return render_template('auth/login.html', message='')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        user = User.query.filter_by(username=username).first()
        if user is not None:
            return render_template('auth/signup.html', message='Пользователь с таким именем уже существует')

        user = User(username=username, password=password)
        db.session.add(user)
        db.session.commit()
        return redirect('/login')

    return render_template('auth/signup.html', message='')


@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')


@app.route('/')
def main():
    is_auth = current_user.is_authenticated
    return render_template('main/main.html', is_auth=is_auth)


@app.route('/universities')
def university_table():
    universities = University.query.all()
    return render_template('universities/table.html', table=universities)


@app.route('/universities/new', methods=['GET', 'POST'])
@login_required
def university_new():
    if request.method == 'POST':
        full_name = request.form['full_name']
        short_name = request.form['short_name']
        foundation_date = request.form['foundation_date']
        university = University(full_name=full_name, short_name=short_name, foundation_date=foundation_date)
        db.session.add(university)
        db.session.commit()
        return redirect('/universities')

    return render_template('universities/new.html', form={})


@app.route('/universities/<int:id>', methods=['GET', 'POST'])
@login_required
def university_update(id):
    university = University.query.get_or_404(id)
    if request.method == 'POST':
        university.full_name = request.form['full_name']
        university.short_name = request.form['short_name']
        university.foundation_date = request.form['foundation_date']
        db.session.commit()
        return redirect('/universities')

    return render_template('universities/new.html', form=university)


@app.route('/universities/<int:id>/delete', methods=['GET'])
@login_required
def university_delete(id):
    University.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/universities')


@app.route('/students')
def students_table():
    students = Student.query.all()
    return render_template('students/table.html', table=students)


@app.route('/students/new', methods=['GET', 'POST'])
@login_required
def students_new():
    universities = University.query.all()
    if request.method == 'POST':
        name = request.form['name']
        birthday = request.form['birthday']
        university_id = request.form['university_id']
        admission_year = request.form['admission_year']
        student = Student(name=name, birthday=birthday, university_id=university_id, admission_year=admission_year)
        db.session.add(student)
        db.session.commit()
        return redirect('/students')

    return render_template('students/new.html', form={}, universities=universities)


@app.route('/students/<int:id>', methods=['GET', 'POST'])
@login_required
def students_update(id):
    universities = University.query.all()
    student = Student.query.get_or_404(id)
    if request.method == 'POST':
        student.name = request.form['name']
        student.birthday = request.form['birthday']
        student.university_id = request.form['university_id']
        student.admission_year = request.form['admission_year']
        db.session.commit()
        return redirect('/students')

    print(student)

    return render_template('students/new.html', form=student, universities=universities)


@app.route('/students/<int:id>/delete', methods=['GET'])
@login_required
def students_delete(id):
    Student.query.filter_by(id=id).delete()
    db.session.commit()
    return redirect('/students')


if __name__ == '__main__':
    app.run()
