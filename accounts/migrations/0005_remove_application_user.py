# Generated by Django 3.0.3 on 2020-03-02 18:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20200228_1500'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='application',
            name='user',
        ),
    ]
