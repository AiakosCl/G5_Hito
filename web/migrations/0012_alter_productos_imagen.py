# Generated by Django 4.2 on 2024-05-07 18:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_alter_productos_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productos',
            name='imagen',
            field=models.ImageField(default='productos/cargar_imagen.png', upload_to='productos/'),
        ),
    ]
