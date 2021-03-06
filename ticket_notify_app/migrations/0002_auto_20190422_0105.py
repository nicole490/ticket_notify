# Generated by Django 2.1.4 on 2019-04-21 16:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('ticket_notify_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='concert',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='作成日時'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='concert',
            name='updated_at',
            field=models.DateTimeField(auto_now=True, verbose_name='更新日時'),
        ),
    ]
