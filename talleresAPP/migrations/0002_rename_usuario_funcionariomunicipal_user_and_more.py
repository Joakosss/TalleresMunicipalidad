# Generated by Django 5.0.6 on 2024-11-13 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('talleresAPP', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='funcionariomunicipal',
            old_name='usuario',
            new_name='user',
        ),
        migrations.RenameField(
            model_name='instructor',
            old_name='usuario',
            new_name='user',
        ),
    ]
