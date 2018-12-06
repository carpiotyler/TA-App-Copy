# Generated by Django 2.1.3 on 2018-11-30 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TAServer', '0003_auto_20181129_2146'),
    ]

    operations = [
        migrations.AlterField(
            model_name='section',
            name='days',
            field=models.CharField(blank=True, choices=[('M', 'Monday'), ('T', 'Tuesday'), ('W', 'Wednesday'), ('H', 'Thursday'), ('F', 'Friday'), ('MW', 'Monday Wednesday'), ('TH', 'Tuesday Thursday'), ('MWF', 'Monday Wednesday Friday')], default=None, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='section',
            name='time',
            field=models.CharField(blank=True, default=None, max_length=15, null=True),
        ),
    ]
