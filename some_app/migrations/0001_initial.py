# Generated by Django 4.0.4 on 2022-05-17 22:17

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Player_choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('player_x', models.CharField(max_length=5, unique=True)),
                ('player_y', models.CharField(max_length=5, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='SignUp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50, unique=True, validators=[django.core.validators.MinLengthValidator(4)])),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('first_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(4)])),
                ('last_name', models.CharField(max_length=50, validators=[django.core.validators.MinLengthValidator(4)])),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Grid_choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grid_choice1', models.CharField(max_length=5)),
                ('grid_choice2', models.CharField(max_length=5)),
                ('grid_choice3', models.CharField(max_length=5)),
                ('grid_choice4', models.CharField(max_length=5)),
                ('grid_choice5', models.CharField(max_length=5)),
                ('grid_choice6', models.CharField(max_length=5)),
                ('grid_choice7', models.CharField(max_length=5)),
                ('grid_choice8', models.CharField(max_length=5)),
                ('grid_choice9', models.CharField(max_length=5)),
                ('timestamp', models.DateTimeField(auto_now_add=True)),
                ('player', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='some_app.player_choice')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='some_app.signup')),
            ],
        ),
    ]
