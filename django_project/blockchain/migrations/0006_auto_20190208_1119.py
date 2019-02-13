# Generated by Django 2.1.5 on 2019-02-08 11:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blockchain', '0005_auto_20190206_2244'),
    ]

    operations = [
        migrations.AddField(
            model_name='input',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blockchain.Transaction'),
        ),
        migrations.AddField(
            model_name='output',
            name='transaction',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blockchain.Transaction'),
        ),
    ]
