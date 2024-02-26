# Generated by Django 4.0 on 2023-09-17 18:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
        ('AcademicTaskManager', '0025_remove_quizsubmission_correctanswers_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='chat',
            old_name='user2',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='chat',
            old_name='user1',
            new_name='teacher',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 20, 57, 23, 831341)),
        ),
        migrations.AlterField(
            model_name='chat',
            name='message',
            field=models.ManyToManyField(blank=True, related_name='chatMessages', to='AcademicTaskManager.Message'),
        ),
        migrations.AlterField(
            model_name='classroom',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='classroomStudents', to='AcademicTaskManager.Student'),
        ),
        migrations.AlterField(
            model_name='course',
            name='major',
            field=models.ManyToManyField(related_name='courseMajor', to='AcademicTaskManager.Major'),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 20, 57, 23, 831341)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='answeredBy',
            field=models.ManyToManyField(blank=True, related_name='answeredby', to='AcademicTaskManager.Student'),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 20, 57, 23, 831341)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='questions',
            field=models.ManyToManyField(related_name='quizQuestions', to='AcademicTaskManager.Question'),
        ),
        migrations.AlterField(
            model_name='student',
            name='passedCourses',
            field=models.ManyToManyField(blank=True, related_name='studentPassedCourses', to='AcademicTaskManager.Course'),
        ),
        migrations.AlterField(
            model_name='student',
            name='registeredCourses',
            field=models.ManyToManyField(blank=True, related_name='studentCourses', to='AcademicTaskManager.Course'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='courses',
            field=models.ManyToManyField(blank=True, related_name='teacherCourses', to='AcademicTaskManager.Course'),
        ),
        migrations.AlterField(
            model_name='user',
            name='groups',
            field=models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.Group', verbose_name='groups'),
        ),
        migrations.AlterField(
            model_name='user',
            name='user_permissions',
            field=models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.Permission', verbose_name='user permissions'),
        ),
    ]
