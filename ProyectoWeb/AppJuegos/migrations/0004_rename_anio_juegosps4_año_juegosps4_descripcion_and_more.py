# Generated by Django 5.0 on 2024-02-04 20:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppJuegos', '0003_avatarimagen'),
    ]

    operations = [
        migrations.RenameField(
            model_name='juegosps4',
            old_name='anio',
            new_name='año',
        ),
        migrations.AddField(
            model_name='juegosps4',
            name='descripcion',
            field=models.CharField(default=django.utils.timezone.now, max_length=300),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='juegosps4',
            name='fecha',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='juegosps4',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenesPS4'),
        ),
    ]
