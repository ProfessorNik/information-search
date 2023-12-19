from django.forms import ModelForm, TextInput, DateInput, ModelChoiceField, NumberInput, Select

from students.models import Student
from universities.models import University


class StudentForm(ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'birthday', 'university', 'admission_year']

        widgets = {
            'name': TextInput(attrs={'maxlength': 100, 'required': 'required'}),
            'birthday': DateInput(
                format='%Y-%m-%d',
                attrs={'required': 'required', 'type': 'date'}),
            'admission_year': NumberInput(attrs={'maxlength': 100, 'required': 'required'})
        }
