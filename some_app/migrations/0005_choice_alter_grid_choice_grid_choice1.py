# Generated by Django 4.0.4 on 2022-05-20 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('some_app', '0004_signup_password'),
    ]

    operations = [
        migrations.CreateModel(
            name='Choice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice1', models.CharField(max_length=5)),
                ('choice2', models.CharField(max_length=5)),
                ('choice3', models.CharField(max_length=5)),
                ('choice4', models.CharField(max_length=5)),
                ('choice5', models.CharField(max_length=5)),
                ('choice6', models.CharField(max_length=5)),
                ('choice7', models.CharField(max_length=5)),
                ('choice8', models.CharField(max_length=5)),
                ('choice9', models.CharField(max_length=5)),
            ],
        ),
        migrations.AlterField(
            model_name='grid_choice',
            name='grid_choice1',
            field=models.ForeignKey(on_delete=django.db.models.deletion.RESTRICT, to='some_app.choice'),
        ),
    ]