# Generated by Django 4.0.4 on 2022-06-06 20:22

from django.db import migrations, models
import some_app.models


class Migration(migrations.Migration):

    dependencies = [
        ('some_app', '0010_alter_todolist_to_do_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='to_do_message',
            field=models.CharField(max_length=20),
        ),
    ]
