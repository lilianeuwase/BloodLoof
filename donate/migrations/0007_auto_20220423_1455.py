# Generated by Django 2.1 on 2022-04-23 14:55

from django.db import migrations
import donate.managers


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0006_auto_20220423_1440'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='donor',
            managers=[
                ('objects1', donate.managers.UserManager()),
            ],
        ),
    ]
