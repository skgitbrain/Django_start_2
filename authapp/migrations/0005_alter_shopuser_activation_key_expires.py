# Generated by Django 3.2.7 on 2021-10-10 11:22

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0004_auto_20211007_0117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shopuser',
            name='activation_key_expires',
            field=models.DateTimeField(default=datetime.datetime(2021, 10, 12, 11, 22, 36, 646435, tzinfo=utc)),
        ),
    ]
