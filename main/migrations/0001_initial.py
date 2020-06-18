# Generated by Django 3.0.7 on 2020-06-18 21:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Card',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('mana_cost', models.CharField(max_length=200)),
                ('card_image_loc', models.CharField(max_length=800)),
                ('power', models.IntegerField()),
                ('toughness', models.IntegerField()),
                ('card_text', models.CharField(max_length=4000)),
                ('flavor_text', models.CharField(max_length=4000)),
                ('set_name', models.CharField(max_length=200)),
                ('artist', models.CharField(max_length=200)),
                ('collection_number', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Card_Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_color', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card_Rarity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_rarity', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Card_Type',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('card_type', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Seller',
            fields=[
                ('seller_key', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('seller_name', models.CharField(max_length=200)),
                ('seller_type', models.CharField(max_length=200)),
                ('completed_sales', models.BigIntegerField()),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_user_id', models.IntegerField()),
                ('price_threshold', models.FloatField()),
                ('less_than_flag', models.BooleanField()),
                ('greater_than_flag', models.BooleanField()),
                ('equal_flag', models.BooleanField()),
                ('selling_auth_user_id', models.IntegerField()),
                ('card_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Card')),
                ('seller_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Seller')),
            ],
        ),
        migrations.CreateModel(
            name='Listing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_line', models.CharField(max_length=50)),
                ('set_name', models.CharField(max_length=200)),
                ('price', models.FloatField()),
                ('quantity', models.IntegerField()),
                ('condition', models.CharField(max_length=200)),
                ('seller_type', models.CharField(max_length=200)),
                ('sponsored', models.BooleanField()),
                ('user_listing', models.BooleanField()),
                ('selling_user_id', models.IntegerField()),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Card')),
                ('seller_key', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Seller')),
            ],
        ),
        migrations.AddField(
            model_name='card',
            name='color_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Card_Color'),
        ),
        migrations.AddField(
            model_name='card',
            name='rarity_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Card_Rarity'),
        ),
        migrations.AddField(
            model_name='card',
            name='type_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Card_Type'),
        ),
        migrations.CreateModel(
            name='Bazaar_User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('auth_user_id', models.IntegerField()),
                ('completed_sales', models.BigIntegerField()),
                ('location_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.Location')),
            ],
        ),
    ]
