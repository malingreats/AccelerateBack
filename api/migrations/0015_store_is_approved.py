# Generated by Django 3.2.9 on 2021-11-22 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0014_auto_20211119_1509'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='is_approved',
            field=models.BooleanField(blank=True, default=False),
        ),
    ]
