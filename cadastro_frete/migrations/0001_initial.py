# Generated by Django 3.0.8 on 2021-10-28 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CadastroCliente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Sem_Nome_Cadastrado', max_length=50)),
                ('doc', models.CharField(max_length=14, unique=True)),
                ('about', models.CharField(max_length=250)),
                ('active', models.BooleanField()),
                ('site', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='CadastroEmpresa',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='Sem_Nome_Cadastrado', max_length=50)),
                ('doc', models.CharField(max_length=14, unique=True)),
                ('about', models.CharField(max_length=250)),
                ('active', models.BooleanField()),
                ('site', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Lance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.CharField(max_length=20)),
                ('amount', models.CharField(max_length=20)),
                ('id_offer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='cadastro_frete.CadastroEmpresa')),
                ('id_provider', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='cadastro_frete.CadastroCliente')),
            ],
        ),
        migrations.CreateModel(
            name='CadastroOferta',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_de', models.CharField(max_length=20)),
                ('to_para', models.CharField(max_length=20)),
                ('initial_value', models.CharField(max_length=20)),
                ('amount', models.CharField(max_length=20)),
                ('amount_type', models.CharField(max_length=10)),
                ('id_customer', models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='cadastro_frete.CadastroCliente')),
            ],
        ),
    ]