# Generated by Django 3.2.7 on 2021-09-09 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cars', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cars',
            name='km_driven',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cars',
            name='seats',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cars',
            name='selling_price',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='cars',
            name='year',
            field=models.CharField(max_length=255),
        ),
    ]