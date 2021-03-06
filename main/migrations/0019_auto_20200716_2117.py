# Generated by Django 3.2 on 2020-07-16 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0018_user_preferences'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_preferences',
            name='allow_email',
        ),
        migrations.AddField(
            model_name='user_preferences',
            name='email_notif',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_preferences',
            name='subscribe_email',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='user_preferences',
            name='view_email',
            field=models.BooleanField(default=False),
        ),
    ]
