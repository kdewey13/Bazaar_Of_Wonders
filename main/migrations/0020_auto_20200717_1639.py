# Generated by Django 3.2 on 2020-07-17 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0019_auto_20200716_2117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_preferences',
            name='email_notif',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user_preferences',
            name='subscribe_email',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='user_preferences',
            name='view_email',
            field=models.BooleanField(default=True),
        ),
    ]
