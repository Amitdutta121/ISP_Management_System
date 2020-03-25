# Generated by Django 3.0.4 on 2020-03-25 21:28

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('isp', '0020_auto_20200326_0327'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invoices',
            name='Date_issued',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 21, 28, 4, 388773, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='invoices',
            name='date_auto_disconnect',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 21, 28, 4, 388773, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='users',
            name='connection_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 21, 28, 4, 333921, tzinfo=utc)),
        ),
    ]
