# Generated by Django 5.0.6 on 2024-11-09 00:24

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('talleresAPP', '0005_alter_taller_descripcion'),
    ]

    operations = [
        migrations.AddField(
            model_name='adultomayor',
            name='email',
            field=models.EmailField(default='a@a.com', max_length=254),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adultomayor',
            name='s_nombre',
            field=models.CharField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='adultomayor',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='talleresAPP.usuario'),
        ),
        migrations.AlterField(
            model_name='funcionariomunicipal',
            name='s_nombre',
            field=models.CharField(blank=True, default='', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='funcionariomunicipal',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='talleresAPP.usuario'),
        ),
        migrations.AlterField(
            model_name='instructor',
            name='s_nombre',
            field=models.CharField(blank=True, default=' ', max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='instructor',
            name='usuario',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='talleresAPP.usuario'),
        ),
    ]
