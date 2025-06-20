# Generated by Django 3.2.19 on 2025-04-26 05:41

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author',
            field=models.CharField(max_length=30, null=True),
        ),
        migrations.AddField(
            model_name='book',
            name='is_bestselling',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='rating',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(1)]),
        ),
    ]
