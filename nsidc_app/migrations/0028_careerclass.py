# Generated by Django 4.0.6 on 2022-07-29 10:38

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('nsidc_app', '0027_enquiryclass_gemclass_panelmentclass_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='careerclass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slno', models.CharField(max_length=2)),
                ('tenderno', models.CharField(max_length=200)),
                ('download', models.URLField(blank=True)),
                ('downloadname', models.CharField(blank=True, max_length=300)),
                ('description', models.CharField(max_length=300)),
                ('releasedate', models.DateTimeField(default=django.utils.timezone.now)),
                ('closingdate', models.DateField()),
            ],
        ),
    ]
