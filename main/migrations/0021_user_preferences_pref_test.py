# Generated by Django 3.2 on 2020-07-17 16:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0020_auto_20200717_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_preferences',
            name='pref_test',
            field=models.CharField(default='testing', max_length=100),
        ),
    ]
