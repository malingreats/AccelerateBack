# Generated by Django 3.2.9 on 2021-11-08 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0010_auto_20211106_1448'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='sdg_goals',
            field=models.CharField(blank=True, default='One', max_length=75, null=True),
        ),
    ]
