# Generated by Django 3.0.4 on 2020-03-25 17:11

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('isp', '0004_auto_20200325_2240'),
    ]

    operations = [
        migrations.CreateModel(
            name='Invoices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('total_balance', models.CharField(max_length=100)),
            ],
        ),
        migrations.AlterField(
            model_name='users',
            name='connection_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 3, 25, 17, 11, 5, 85400, tzinfo=utc)),
        ),
        migrations.CreateModel(
            name='UserAndinvoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isp.Invoices')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='isp.Users')),
            ],
        ),
    ]
