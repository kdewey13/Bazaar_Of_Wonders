# Generated by Django 3.2 on 2020-07-18 22:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0025_alter_notification_unique_together'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='notification',
            name='seller_key',
        ),
    ]
