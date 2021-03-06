# Generated by Django 3.0.8 on 2020-07-24 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0026_remove_notification_seller_key'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='card',
            name='tcgplayer_id',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='card_market_purchase_url',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='mtg_stocks_purchase_url',
        ),
        migrations.RemoveField(
            model_name='listing',
            name='tcg_player_purchase_url',
        ),
        migrations.AddField(
            model_name='card',
            name='card_market_purchase_url',
            field=models.CharField(default='https://www.cardmarket.com/en', max_length=2000),
        ),
        migrations.AddField(
            model_name='card',
            name='last_updated',
            field=models.CharField(default='2020-07-24T22:26:54.398741', max_length=200),
        ),
        migrations.AddField(
            model_name='card',
            name='mtg_stocks_purchase_url',
            field=models.CharField(default='https://www.mtgstocks.com/news', max_length=2000),
        ),
        migrations.AddField(
            model_name='card',
            name='scryfall_id',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='card',
            name='tcg_player_purchase_url',
            field=models.CharField(default='https://www.tcgplayer.com/', max_length=2000),
        ),
        migrations.AddField(
            model_name='listing',
            name='last_updated',
            field=models.CharField(default='2020-07-24T22:26:54.402972', max_length=200),
        ),
    ]
