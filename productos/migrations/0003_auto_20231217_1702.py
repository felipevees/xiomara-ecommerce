# Generated by Django 3.2.23 on 2023-12-17 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('productos', '0002_alter_imagenproducto_imagen'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='producto',
            name='imagenes',
        ),
        migrations.AddField(
            model_name='imagenproducto',
            name='producto',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='imagenes', to='productos.producto'),
            preserve_default=False,
        ),
    ]