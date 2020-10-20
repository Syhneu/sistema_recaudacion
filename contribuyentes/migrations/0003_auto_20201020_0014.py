# Generated by Django 3.1.1 on 2020-10-20 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('contribuyentes', '0002_auto_20201019_1250'),
    ]

    operations = [
        migrations.CreateModel(
            name='RcRepresentante',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=12)),
                ('nr_civi', models.CharField(max_length=100)),
                ('nombre', models.TextField()),
                ('cargo', models.TextField()),
                ('direccion', models.TextField()),
                ('telefono', models.TextField()),
                ('cod_con', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=30)),
            ],
        ),
        migrations.RemoveField(
            model_name='rccontrib',
            name='id',
        ),
        migrations.AlterField(
            model_name='rccontrib',
            name='cod_con',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='rccontrib',
            name='fec_inicio',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='rccontrib',
            name='tipo_persona',
            field=models.CharField(choices=[('J', 'Juridica'), ('N', 'Natural'), ('G', 'Gobierno')], default='J', max_length=1),
        ),
        migrations.CreateModel(
            name='RcAccionistas',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cedula', models.CharField(max_length=12)),
                ('nombre', models.TextField()),
                ('nr_civi', models.TextField()),
                ('cargo', models.TextField()),
                ('direccion', models.TextField()),
                ('telefono', models.CharField(max_length=11)),
                ('cod_con', models.IntegerField()),
                ('correo', models.EmailField(max_length=254)),
                ('celular', models.CharField(max_length=11)),
                ('cod_repre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contribuyentes.rccontrib')),
            ],
        ),
    ]