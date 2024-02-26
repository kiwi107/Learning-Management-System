# Generated by Django 4.0 on 2023-09-17 19:47

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('AcademicTaskManager', '0027_alter_announcement_date_alter_message_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='announcement',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 21, 47, 6, 402995)),
        ),
        migrations.AlterField(
            model_name='message',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 21, 47, 6, 402995)),
        ),
        migrations.AlterField(
            model_name='quiz',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2023, 9, 17, 21, 47, 6, 402995)),
        ),
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('message', models.ManyToManyField(blank=True, related_name='chatMessages', to='AcademicTaskManager.Message')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user2', to='AcademicTaskManager.user')),
                ('teacher', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user1', to='AcademicTaskManager.user')),
            ],
        ),
    ]