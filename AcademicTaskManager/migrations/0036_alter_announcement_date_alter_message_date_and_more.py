# Generated by Django 4.0 on 2023-09-19 21:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0035_assignmentsubmission_submittedby_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 19, 23, 37, 50, 873173)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 19, 23, 37, 50, 873173)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 19, 23, 37, 50, 870183)),
        ),
    ]
