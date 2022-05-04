# Generated by Django 2.1 on 2022-05-02 17:56

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('authentication', '0003_delete_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=100, null=True, unique=True, verbose_name='username')),
                ('fname', models.CharField(blank=True, max_length=30, verbose_name='first name')),
                ('lname', models.CharField(blank=True, max_length=30, verbose_name='last name')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('password', models.CharField(blank=True, max_length=30, verbose_name='password')),
                ('phone_number', models.CharField(blank=True, max_length=14, verbose_name='phone number')),
                ('is_donor', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('house_address', models.TextField(max_length=200)),
            ],
            options={
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]