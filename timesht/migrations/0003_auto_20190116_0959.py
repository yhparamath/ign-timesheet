# Generated by Django 2.0.10 on 2019-01-16 09:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('timesht', '0002_ename_date'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ename',
            name='date',
        ),
        migrations.AddField(
            model_name='ename',
            name='entry_date',
            field=models.DateField(default=datetime.date(2019, 1, 16)),
        ),
    ]
