# Generated by Django 4.2.2 on 2023-06-14 18:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=60)),
                ('number', models.IntegerField(null=True)),
                ('complement', models.CharField(max_length=50)),
                ('district', models.CharField(max_length=20)),
                ('city', models.CharField(max_length=20)),
                ('state', models.CharField(blank=True, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('email', models.CharField(blank=True, max_length=60)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Theme',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=10)),
                ('price', models.FloatField()),
                ('itens', models.ManyToManyField(related_name='themes', to='aluguel_de_temas.item')),
            ],
        ),
        migrations.CreateModel(
            name='Rent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('start_hours', models.CharField(max_length=5)),
                ('end_hours', models.CharField(max_length=5)),
                ('address', models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='aluguel_de_temas.address')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='aluguel_de_temas.client')),
                ('theme', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rents', to='aluguel_de_temas.theme')),
            ],
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ddd', models.CharField(max_length=3)),
                ('number', models.CharField(max_length=10)),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='phones', to='aluguel_de_temas.client')),
            ],
        ),
    ]