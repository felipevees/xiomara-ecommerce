# Generated by Django 3.2.23 on 2023-12-17 21:47

from django.db import migrations, models
import productos.models


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagenproducto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to=productos.models.get_image_path),
        ),
    ]