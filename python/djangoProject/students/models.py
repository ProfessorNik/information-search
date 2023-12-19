from django.db import models

from universities.models import University


# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    birthday = models.DateField(max_length=100)
    university = models.ForeignKey(University, on_delete=models.PROTECT)
    admission_year = models.IntegerField(default=None)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/students/'

    class Meta:
        verbose_name_plural = "Students",
        verbose_name = "Student"
