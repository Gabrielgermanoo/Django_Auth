# Generated by Django 4.0.5 on 2022-06-30 17:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comp', '0006_alter_login_login'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='login',
            field=models.CharField(max_length=50),
        ),
    ]
