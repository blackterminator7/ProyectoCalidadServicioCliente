# Generated by Django 3.1.7 on 2021-05-05 05:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyecto', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='encuestacliente',
            name='id_encuestaCliente',
        ),
        migrations.RemoveField(
            model_name='encuestapersonal',
            name='id_encuestaPersonal',
        ),
        migrations.AddField(
            model_name='encuestacliente',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='encuestapersonal',
            name='id',
            field=models.AutoField(auto_created=True, default=5, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
    ]