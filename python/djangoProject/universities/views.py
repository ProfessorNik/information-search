from django.shortcuts import render, redirect
from django.views.generic import UpdateView

from universities.Forms import UniversityForm
from universities.models import University


# Create your views here.

class UniversityUpdateView(UpdateView):
    model = University
    template_name = 'universities/new.html'
    context_object_name = 'form'
    form_class = UniversityForm


def table(request):
    universities = University.objects.all()
    return render(request, 'universities/table.html', {'table': universities})


def new(request):
    error = ''
    if request.method == 'POST':
        form = UniversityForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/universities')
        else:
            error = "Форма заполнена не верно"

    form = UniversityForm()
    return render(request, 'universities/new.html', {'form': form, 'error': error})


def delete(request, pk):
    University.objects.filter(id=pk).delete()
    return redirect('/universities')
