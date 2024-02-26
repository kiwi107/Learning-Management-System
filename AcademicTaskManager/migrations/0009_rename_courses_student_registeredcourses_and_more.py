# Generated by Django 4.2.5 on 2023-09-11 20:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0008_question_rename_submission_assignmentsubmission_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='courses',
            new_name='registeredCourses',
        ),
        migrations.AlterField(
            model_name='quiz',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizzesCourse', to='AcademicTaskManager.course'),
        ),
    ]