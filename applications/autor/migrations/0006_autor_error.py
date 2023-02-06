# Generated by Django 4.1.2 on 2023-01-17 14:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('autor', '0005_alter_autor_edad'),
    ]

    operations = [
        migrations.AddConstraint(
            model_name='autor',
            constraint=models.CheckConstraint(check=models.Q(('nacimiento__lte', models.F('muerte'))), name='error'),
        ),
    ]
