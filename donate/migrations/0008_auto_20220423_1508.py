# Generated by Django 2.1 on 2022-04-23 15:08

from django.db import migrations
import donate.managers


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0007_auto_20220423_1455'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='donor',
            managers=[
                ('objects', donate.managers.UserManager()),
            ],
        ),
    ]
