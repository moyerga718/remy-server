# Generated by Django 4.1 on 2022-09-01 20:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remyapi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='starting_item',
            field=models.BooleanField(default=False),
        ),
    ]
