# Generated by Django 3.0.8 on 2020-07-29 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0027_auto_20200724_2226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='last_updated',
            field=models.CharField(default='2020-07-29T07:00:06.318782', max_length=200),
        ),
        migrations.AlterField(
            model_name='listing',
            name='last_updated',
            field=models.CharField(default='2020-07-29T07:00:06.319966', max_length=200),
        ),
    ]
