# Generated by Django 4.2.5 on 2023-10-07 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0004_alter_dish_price'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Profile',
        ),
    ]