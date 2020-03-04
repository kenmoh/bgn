# Generated by Django 3.0.3 on 2020-02-28 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('pages', '0003_post_date_posted'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=125)),
                ('content', models.TextField()),
                ('url', models.URLField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('video', models.FileField(blank=True, null=True, upload_to='')),
                ('date_posted', models.DateTimeField(auto_now_add=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]