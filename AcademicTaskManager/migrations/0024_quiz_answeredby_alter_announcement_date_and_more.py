# Generated by Django 4.2.5 on 2023-09-17 03:49

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0023_alter_announcement_date_alter_quiz_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='answeredBy',
            field=models.ManyToManyField(blank=True, related_name='answeredby', to='AcademicTaskManager.student'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 5, 49, 15, 574546)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 5, 49, 15, 572544)),
        ),
    ]