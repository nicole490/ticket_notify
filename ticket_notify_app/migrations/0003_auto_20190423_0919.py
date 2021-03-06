# Generated by Django 2.1.4 on 2019-04-23 00:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_notify_app', '0002_auto_20190422_0105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concert',
            name='artist_id',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='アーティストid'),
        ),
        migrations.AlterField(
            model_name='concert',
            name='max_price',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0)], verbose_name='価格'),
        ),
    ]
