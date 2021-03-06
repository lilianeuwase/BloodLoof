# Generated by Django 2.1 on 2022-04-23 12:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Donors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('phone_number', models.CharField(max_length=14, unique=True)),
                ('date_of_birth', models.DateField(max_length=14)),
                ('Weight', models.DecimalField(decimal_places=2, max_digits=5)),
                ('Height', models.DecimalField(decimal_places=3, max_digits=5)),
                ('Aval_Time', models.DateTimeField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
