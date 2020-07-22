# Generated by Django 3.2 on 2020-07-18 22:22

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main', '0024_auto_20200718_2213'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='notification',
            unique_together={('auth_user_id', 'card_id', 'price_threshold')},
        ),
    ]