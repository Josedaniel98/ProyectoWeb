# Generated by Django 2.2.6 on 2019-10-16 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20191016_1745'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formulario',
            name='nombre',
            field=models.CharField(max_length=60),
        ),
    ]