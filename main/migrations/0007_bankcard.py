# Generated by Django 4.2.1 on 2023-06-03 11:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_tiket_departure_alter_country_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankCard',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('surname', models.TextField()),
                ('mail', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=50)),
                ('card_number', models.CharField(max_length=16)),
                ('cardholder_name', models.TextField()),
                ('validity', models.DateField()),
                ('cvv', models.CharField(max_length=3)),
            ],
        ),
    ]
