# Generated by Django 4.1.7 on 2023-04-01 03:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_alter_pokemon_table_alter_pokemontypes_table'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pokemon',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]
