from django.db import models


# Create your models here.

class University(models.Model):
    full_name = models.CharField(max_length=100)
    short_name = models.CharField(max_length=100)
    foundation_date = models.DateField()

    def __str__(self):
        return self.short_name

    def get_absolute_url(self):
        return '/universities/'

    class Meta:
        verbose_name = 'University'
        verbose_name_plural = "Universities"
