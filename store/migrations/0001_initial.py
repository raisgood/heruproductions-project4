# Generated by Django 3.0.2 on 2021-02-23 23:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('director', models.CharField(max_length=200)),
                ('writer', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('publish_date', models.DateField(default=datetime.date.today)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('stock', models.IntegerField(default=0)),
            ],
        ),
    ]
