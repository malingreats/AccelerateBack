# Generated by Django 3.2.8 on 2021-11-04 23:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_auto_20211104_0419'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='rating',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]
