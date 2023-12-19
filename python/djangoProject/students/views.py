from django.shortcuts import render, redirect
from django.views.generic import UpdateView, CreateView

from students.Forms import StudentForm
from students.models import Student


class StudentsUpdateView(UpdateView):
    model = Student
    template_name = 'students/new.html'
    context_object_name = 'form'
    form_class = StudentForm


class StudentsCreateView(CreateView):
    model = Student
    template_name = 'students/new.html'
    context_object_name = 'form'
    form_class = StudentForm


def table(request):
    students_table = Student.objects.all()
    return render(request, 'students/table.html', {'table': students_table})


def delete(request, pk):
    Student.objects.filter(id=pk).delete()
    return redirect('/students')
