# Generated by Django 4.2.5 on 2023-10-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0002_profile_address'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.TextField(max_length=100)),
                ('image', models.ImageField(default='default.jpg', upload_to='dish_pics')),
            ],
        ),
    ]
