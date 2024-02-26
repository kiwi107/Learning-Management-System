# Generated by Django 4.2.5 on 2023-09-08 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0006_course_major'),
    ]

    operations = [
        migrations.AddField(
            model_name='classroom',
            name='semester',
            field=models.CharField(choices=[('Fall', 'Fall'), ('Spring', 'Spring'), ('Summer', 'Summer')], default='Fall', max_length=10),
        ),
        migrations.AddField(
            model_name='course',
            name='creditHours',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='course',
            name='grade',
            field=models.CharField(blank=True, choices=[('In Progress', 'In Progress'), ('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], default='In Progress', max_length=20),
        ),
        migrations.AddField(
            model_name='major',
            name='totalCreditHours',
            field=models.IntegerField(default=120),
        ),
        migrations.AddField(
            model_name='student',
            name='passedCourses',
            field=models.ManyToManyField(blank=True, related_name='studentPassedCourses', to='AcademicTaskManager.course'),
        ),
    ]