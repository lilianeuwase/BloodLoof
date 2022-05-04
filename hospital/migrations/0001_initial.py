# Generated by Django 2.1 on 2022-04-25 10:36

from django.db import migrations, models
import hospital.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Hospital',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=14, null=True, unique=True)),
                ('hospital_name', models.CharField(max_length=40, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
            ],
            options={
                'abstract': False,
            },
            # managers=[
            #     ('objects', hospital.managers.UserManager()),
            # ],
        ),
    ]