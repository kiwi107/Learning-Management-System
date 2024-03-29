# Generated by Django 4.0 on 2023-09-17 23:15

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0030_alter_announcement_date_alter_message_date_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='img',
            field=models.ImageField(default='images/student.png', upload_to='images/'),
        ),
        migrations.AddField(
            model_name='teacher',
            name='img',
            field=models.ImageField(default='images/teacher.svg', upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 18, 1, 15, 47, 477268)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 18, 1, 15, 47, 477268)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 18, 1, 15, 47, 475279)),
        ),
    ]
