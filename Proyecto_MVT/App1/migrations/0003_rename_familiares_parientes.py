# Generated by Django 4.1.3 on 2022-11-07 13:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("App1", "0002_familiares_delete_amigos"),
    ]

    operations = [
        migrations.RenameModel(old_name="Familiares", new_name="Parientes",),
    ]