# Generated by Django 2.1 on 2022-04-23 13:40

from django.db import migrations
import donate.managers


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0004_auto_20220423_1330'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='donor',
            managers=[
                ('objects', donate.managers.UserManager()),
            ],
        ),
    ]
