from django.forms import ModelForm, TextInput, DateInput

from universities.models import University


class UniversityForm(ModelForm):
    class Meta:
        model = University
        fields = ['full_name', 'short_name', 'foundation_date']

        widgets = {
            'full_name': TextInput(attrs={'maxlength': 100, 'required': 'required'}),
            'short_name': TextInput(attrs={'maxlength': 100, 'required': 'required'}),
            'foundation_date': DateInput(
                format='%Y-%m-%d',
                attrs={'required': 'required', 'type': 'date'})
        }

