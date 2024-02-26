# Generated by Django 4.0 on 2023-09-22 01:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0040_assignmentsubmission_late_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignmentsubmission',
            name='submittedBy',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 22, 3, 31, 54, 376489)),
        ),
        migrations.AlterField(
            model_name='assignmentsubmission',
            name='submissionTime',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 22, 3, 31, 54, 372502)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 22, 3, 31, 54, 376489)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 22, 3, 31, 54, 373499)),
        ),
    ]
