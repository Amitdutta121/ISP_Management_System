# Generated by Django 3.0.4 on 2020-03-25 16:38

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('isp', '0002_auto_20200325_2234'),
    ]

    operations = [
        migrations.CreateModel(
            name='Packages',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bandwidth', models.CharField(max_length=500)),
                ('extra_information', models.TextField()),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='connection_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 16, 38, 9, 867100, tzinfo=utc)),
        ),
    ]
