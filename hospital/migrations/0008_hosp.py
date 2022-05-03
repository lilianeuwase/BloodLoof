# Generated by Django 2.1 on 2022-05-02 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0007_auto_20220502_1640'),
    ]

    operations = [
        migrations.CreateModel(
            name='Hosp',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.CharField(max_length=100, null=True, unique=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
