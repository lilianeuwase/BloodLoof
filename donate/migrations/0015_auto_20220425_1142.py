# Generated by Django 2.1 on 2022-04-25 11:42

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('donate', '0014_auto_20220425_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='id',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]