# Generated by Django 3.2.10 on 2022-02-26 02:35

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authnapp', '0006_alter_shopuser_activation_key_expires'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 28, 2, 35, 21, 210466, tzinfo=utc), verbose_name='актуальность ключа'),
        ),
    ]
