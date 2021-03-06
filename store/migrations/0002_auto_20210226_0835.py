# Generated by Django 3.0.2 on 2021-02-26 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='price',
            field=models.DecimalField(decimal_places=2, default=5.99, max_digits=8),
            preserve_default=False,
        ),

        migrations.AddField(
            model_name='library',
            name='director',
            field=models.CharField(max_length=200),
        ),
        
        migrations.AlterField(
            model_name='library',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='library',
            name='writer',
            field=models.CharField(max_length=200),
        ),
    ]
