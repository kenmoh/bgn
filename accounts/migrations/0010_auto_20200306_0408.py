# Generated by Django 3.0.4 on 2020-03-06 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0009_auto_20200304_1532'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='confirm_application',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='user',
            name='is_approved',
            field=models.BooleanField(default=False),
        ),
        migrations.DeleteModel(
            name='Application',
        ),
    ]