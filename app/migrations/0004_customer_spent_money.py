# Generated by Django 2.2.10 on 2021-07-20 07:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20210719_1708'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='spent_money',
            field=models.FloatField(blank=True, null=True),
        ),
    ]