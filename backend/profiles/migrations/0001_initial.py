# Generated by Django 3.1.7 on 2021-02-23 18:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='RoleSalary',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('preferred_role', models.CharField(choices=[('Web Frontend', 'Web Frontend'), ('Web Backend', 'Web Backend'), ('Fullstack (BE Heavy)', 'Fullstack Be'), ('Fullstack (FE Heavy)', 'Fullstack Fe'), ('Mobile', 'Mobile'), ('Machine Learning', 'Machine Learning'), ('DevOps', 'Devops'), ('Other', 'Other')], max_length=50)),
                ('current_salary', models.CharField(max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Role and Salary',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('country', models.CharField(max_length=255)),
                ('phone', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('github_link', models.CharField(blank=True, max_length=255, null=True)),
                ('linkedin_link', models.CharField(blank=True, max_length=255, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('years_of_experience', models.IntegerField()),
                ('years_of_remote_experience', models.IntegerField()),
                ('english_proficiency', models.CharField(choices=[('Great', 'Great'), ('Average', 'Average'), ('Basic', 'Basic')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Experience',
            },
        ),
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('degree', models.CharField(max_length=255)),
                ('college', models.CharField(max_length=255)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Education',
            },
        ),
        migrations.CreateModel(
            name='Availability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('availability_type', models.CharField(choices=[('Not Available', 'Not Available'), ('Part Time', 'Part Time'), ('Full Time', 'Full Time'), ('Pre FullTime', 'Pre Fulltime')], max_length=50)),
                ('ready_to_start_in', models.CharField(choices=[('now', 'Now'), ('in 1 week', 'In 1 Week'), ('in 2 weeks', 'In 2 Weeks'), ('in 1 month', 'In 1 Month'), ('more than 1 month', 'More Than 1 Month')], max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Availability',
            },
        ),
    ]
