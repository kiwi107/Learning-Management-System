# Generated by Django 4.2.5 on 2023-09-14 18:37

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0017_assignment_submitted_alter_announcement_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assignment',
            name='submitted',
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 14, 20, 37, 26, 709989)),
        ),
    ]