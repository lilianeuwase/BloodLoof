# Generated by Django 2.1 on 2022-04-24 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0012_donor_hospital'),
    ]

    operations = [
        migrations.AddField(
            model_name='donor',
            name='address',
            field=models.CharField(max_length=14, null=True),
        ),
    ]