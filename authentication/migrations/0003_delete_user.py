# Generated by Django 2.1 on 2022-05-02 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_auto_20220502_1656'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
    ]