# Generated by Django 3.0.4 on 2020-03-10 19:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0014_remove_backgroundadmin_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sponsor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=75)),
                ('images', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
            ],
        ),
    ]
