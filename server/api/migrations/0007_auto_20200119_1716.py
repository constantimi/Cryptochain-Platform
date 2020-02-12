# Generated by Django 2.2.6 on 2020-01-19 17:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0006_auto_20200119_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='block',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 19, 17, 16, 15, 839209, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='block',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 19, 17, 16, 15, 839383, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='date_posted',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 19, 17, 16, 15, 839915, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='time',
            field=models.DateTimeField(default=datetime.datetime(2020, 1, 19, 17, 16, 15, 840028, tzinfo=utc)),
        ),
    ]