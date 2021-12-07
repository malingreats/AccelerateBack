# Generated by Django 3.2.9 on 2021-12-07 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0017_store_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='store',
            name='business_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='store',
            name='desc',
            field=models.TextField(blank=True, null=True),
        ),
    ]
