# Generated by Django 2.1.15 on 2021-02-27 15:07

import CoreApp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CoreApp', '0004_recipe'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.ImageField(null=True, upload_to=CoreApp.models.recipe_image_file_path),
        ),
    ]
