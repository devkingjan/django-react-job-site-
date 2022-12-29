# Generated by Django 3.1.7 on 2021-02-26 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('profiles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('phone', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('website', models.CharField(blank=True, max_length=255)),
                ('linkedin_link', models.CharField(blank=True, max_length=255)),
                ('twitter_link', models.CharField(blank=True, max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Company Profile',
            },
        ),
    ]
