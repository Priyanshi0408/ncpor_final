# Generated by Django 4.0.6 on 2022-07-28 08:13

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nsidc_app', '0021_alter_archiveclass_releasedate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='archiveclass',
            name='releasedate',
            field=models.DateField(default=datetime.date(2022, 7, 28)),
        ),
        migrations.AlterField(
            model_name='myclass',
            name='releasedate',
            field=models.DateField(default=datetime.date(2022, 7, 28)),
        ),
    ]
