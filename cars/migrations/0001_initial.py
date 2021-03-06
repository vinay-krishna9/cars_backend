# Generated by Django 3.2.7 on 2021-09-09 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cars',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('year', models.IntegerField(default=0)),
                ('selling_price', models.BigIntegerField(default=0)),
                ('km_driven', models.BigIntegerField(default=0)),
                ('fuel', models.CharField(max_length=255)),
                ('seller_type', models.CharField(max_length=255)),
                ('transmission', models.CharField(max_length=255)),
                ('owner', models.CharField(max_length=255)),
                ('mileage', models.CharField(max_length=255)),
                ('engine', models.CharField(max_length=255)),
                ('max_power', models.CharField(max_length=255)),
                ('torque', models.CharField(max_length=255)),
                ('seats', models.IntegerField(default=0)),
            ],
        ),
    ]
