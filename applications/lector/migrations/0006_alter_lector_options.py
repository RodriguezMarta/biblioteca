# Generated by Django 4.1.2 on 2023-01-17 14:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lector', '0005_alter_lector_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='lector',
            options={'verbose_name': 'Lector', 'verbose_name_plural': 'Lectores'},
        ),
    ]