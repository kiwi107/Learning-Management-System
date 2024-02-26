# Generated by Django 4.2.5 on 2023-09-17 02:22

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0021_alter_announcement_date_alter_quiz_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 4, 22, 6, 887187)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 4, 22, 6, 886190)),
        ),
        migrations.CreateModel(
            name='QuizSubmission',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('marks', models.TextField(default='Not Graded')),
                ('graded', models.BooleanField(default=False)),
                ('correctAnswers', models.ManyToManyField(related_name='correctAnswers', to='AcademicTaskManager.question')),
                ('quiz', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='quizSubmissions', to='AcademicTaskManager.quiz')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='studentQuizSubmissions', to='AcademicTaskManager.student')),
            ],
        ),
    ]
