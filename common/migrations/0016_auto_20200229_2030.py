# Generated by Django 3.0.2 on 2020-02-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0015_auto_20200229_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attendance',
            name='reason',
            field=models.CharField(blank=True, max_length=200),
        ),
        migrations.AlterField(
            model_name='attendance',
            name='type',
            field=models.IntegerField(default=0),
        ),
    ]
