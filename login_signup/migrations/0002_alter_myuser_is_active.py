# Generated by Django 4.0.2 on 2022-02-19 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login_signup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myuser',
            name='is_active',
            field=models.BooleanField(default=True),
        ),
    ]
