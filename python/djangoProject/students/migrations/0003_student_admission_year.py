# Generated by Django 5.0 on 2023-12-14 19:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_alter_student_options_alter_student_birthday_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='admission_year',
            field=models.IntegerField(default=None),
        ),
    ]
