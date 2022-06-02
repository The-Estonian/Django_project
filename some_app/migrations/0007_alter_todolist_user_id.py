# Generated by Django 4.0.4 on 2022-06-01 00:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('some_app', '0006_alter_todolist_done_or_not'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]