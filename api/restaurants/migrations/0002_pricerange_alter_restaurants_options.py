# Generated by Django 5.1.3 on 2025-03-07 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurants', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PriceRange',
            fields=[
                ('idx', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
            options={
                'db_table': 'price_ranges',
                'managed': False,
            },
        ),
        migrations.AlterModelOptions(
            name='restaurants',
            options={},
        ),
    ]
