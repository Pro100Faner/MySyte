# Generated by Django 2.2.6 on 2019-11-10 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mems', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mempost',
            name='image',
            field=models.ImageField(null=True, upload_to='images/', verbose_name='Изображение'),
        ),
    ]