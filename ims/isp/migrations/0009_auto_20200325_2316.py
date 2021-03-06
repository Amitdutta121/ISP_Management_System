# Generated by Django 3.0.4 on 2020-03-25 17:16

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('isp', '0008_auto_20200325_2315'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoices',
            name='date_auto_disconnect',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 17, 16, 22, 522411, tzinfo=utc)),
        ),
        migrations.AddField(
            model_name='invoices',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='invoices',
            name='Date_issued',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 17, 16, 22, 522411, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='connection_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 17, 16, 22, 473514, tzinfo=utc)),
        ),
    ]
