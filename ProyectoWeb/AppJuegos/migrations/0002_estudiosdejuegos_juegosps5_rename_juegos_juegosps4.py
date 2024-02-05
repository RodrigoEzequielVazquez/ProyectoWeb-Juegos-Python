# Generated by Django 5.0 on 2024-01-07 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AppJuegos', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EstudiosDeJuegos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('lanzamientosFamosos', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='JuegosPS5',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('genero', models.CharField(max_length=30)),
                ('anio', models.IntegerField()),
            ],
        ),
        migrations.RenameModel(
            old_name='Juegos',
            new_name='JuegosPS4',
        ),
    ]