# Generated by Django 2.2.10 on 2021-07-18 08:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first', models.FloatField(null=True)),
                ('second', models.FloatField(null=True)),
                ('spent_money', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Deals',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customer', models.TextField(max_length=30)),
                ('item', models.TextField(max_length=50)),
                ('total', models.FloatField(blank=True, null=True)),
                ('quantity', models.FloatField(blank=True, null=True)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
