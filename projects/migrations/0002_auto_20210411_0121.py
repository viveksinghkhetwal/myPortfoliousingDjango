# Generated by Django 3.1.7 on 2021-04-10 19:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Mymodel',
            new_name='Project',
        ),
    ]