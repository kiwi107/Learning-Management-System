# Generated by Django 4.0 on 2023-09-22 01:44

import datetime
from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0041_remove_assignmentsubmission_submittedby_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 22, 3, 44, 55, 545903)),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='submissionTime',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 22, 3, 44, 55, 545903)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 22, 3, 44, 55, 539923)),
        ),
    ]
