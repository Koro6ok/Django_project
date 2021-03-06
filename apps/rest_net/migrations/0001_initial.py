# Generated by Django 3.2.5 on 2021-07-29 21:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('city', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'місто',
                'verbose_name_plural': 'міста',
            },
        ),
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('country', models.CharField(max_length=40)),
            ],
            options={
                'verbose_name': 'Країна',
                'verbose_name_plural': 'Країни',
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=69)),
            ],
            options={
                'verbose_name': 'Стрва',
                'verbose_name_plural': 'страви',
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
            options={
                'verbose_name': 'меню',
            },
        ),
        migrations.CreateModel(
            name='Staff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=255)),
                ('position', models.CharField(blank=True, choices=[('administrator', 'administrator'), ('officiant', 'officiant'), ('cooker', 'cooker'), ('cleaner', 'cleaner')], max_length=50)),
            ],
            options={
                'verbose_name': 'Працівник',
                'verbose_name_plural': 'Персонал',
            },
        ),
        migrations.CreateModel(
            name='Restik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('city', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rest_net.city')),
                ('country', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rest_net.country')),
                ('dish', models.ManyToManyField(to='rest_net.Dish')),
                ('menu', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='rest_net.menu')),
                ('staff', models.ManyToManyField(to='rest_net.Staff')),
            ],
            options={
                'verbose_name': 'Мережа ресторанів',
                'verbose_name_plural': 'Мережі ресторанів',
            },
        ),
    ]
