# Generated by Django 2.2.6 on 2019-10-12 23:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20191004_1628'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id_Carrera', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Catedratico',
            fields=[
                ('id_Catedratico', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Formulario',
            fields=[
                ('id_form', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('mensaje', models.CharField(max_length=350)),
            ],
        ),
        migrations.RemoveField(
            model_name='estudiante',
            name='curso',
        ),
        migrations.AlterField(
            model_name='curso',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Carrera'),
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id_login', models.IntegerField(primary_key=True, serialize=False)),
                ('contrasenia', models.CharField(max_length=30)),
                ('id_catedratico', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Catedratico')),
                ('id_estudiante', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='CursoLibre',
            fields=[
                ('id_CursoLibre', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('horario', models.CharField(max_length=50)),
                ('catedratico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Catedratico')),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionCursoLibre',
            fields=[
                ('id_asignacionlibre', models.IntegerField(primary_key=True, serialize=False)),
                ('cursolibre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.CursoLibre')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Estudiante')),
            ],
        ),
        migrations.CreateModel(
            name='AsignacionCurso',
            fields=[
                ('id_asignacion', models.IntegerField(primary_key=True, serialize=False)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Curso')),
                ('estudiante', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Estudiante')),
            ],
        ),
        migrations.AddField(
            model_name='curso',
            name='catedratico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Catedratico'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='estudiante',
            name='carrera',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app.Carrera'),
            preserve_default=False,
        ),
    ]