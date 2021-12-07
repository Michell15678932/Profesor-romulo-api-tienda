# Generated by Django 3.2.6 on 2021-08-25 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalogo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Area',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('codigoArea', models.CharField(default='', max_length=7, unique=True)),
                ('nombreArea', models.CharField(default='', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Vendedor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dniVendedor', models.CharField(max_length=8, unique=True)),
                ('nombreVendedor', models.CharField(max_length=255)),
                ('comisionVendedor', models.FloatField()),
            ],
        ),
    ]
