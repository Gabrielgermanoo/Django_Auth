# Generated by Django 4.0.5 on 2022-06-23 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0002_alter_users_table'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='Login',
        ),
    ]
