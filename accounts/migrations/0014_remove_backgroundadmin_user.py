# Generated by Django 3.0.4 on 2020-03-08 15:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0013_auto_20200306_0718'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='backgroundadmin',
            name='user',
        ),
    ]
