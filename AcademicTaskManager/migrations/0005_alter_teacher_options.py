# Generated by Django 4.2.5 on 2023-09-08 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0004_alter_student_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'verbose_name': 'Teacher', 'verbose_name_plural': 'Teachers'},
        ),
    ]
