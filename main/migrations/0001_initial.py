# Generated by Django 4.1.2 on 2022-10-26 23:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=25)),
                ('email', models.CharField(max_length=25)),
                ('endereco', models.CharField(max_length=25)),
            ],
        ),
        migrations.CreateModel(
            name='Filme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=25)),
                ('ano_lancamento', models.DateTimeField()),
                ('valor_locacao', models.DecimalField(decimal_places=2, max_digits=4)),
                ('categoria', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.categoria')),
            ],
        ),
        migrations.CreateModel(
            name='Locacao',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrega', models.DateTimeField()),
                ('data_locacao', models.DateTimeField()),
                ('valor', models.DecimalField(decimal_places=2, max_digits=4)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='LocacaoFilme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Locacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.locacao')),
                ('filme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.filme')),
            ],
        ),
        migrations.AddField(
            model_name='locacao',
            name='filme',
            field=models.ManyToManyField(through='main.LocacaoFilme', to='main.filme'),
        ),
    ]
