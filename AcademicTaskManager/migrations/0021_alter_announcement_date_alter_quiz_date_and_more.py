# Generated by Django 4.2.5 on 2023-09-17 02:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0020_quiz_date_quiz_title_alter_announcement_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 4, 20, 50, 199866)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 4, 20, 50, 198869)),
        ),
        migrations.DeleteModel(
            name='QuizSubmission',
        ),
    ]
