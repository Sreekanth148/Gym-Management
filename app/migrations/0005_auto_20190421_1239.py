# Generated by Django 2.1.7 on 2019-04-21 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_auto_20190421_1207'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration_details',
            name='id',
        ),
        migrations.AlterField(
            model_name='registration_details',
            name='email',
            field=models.EmailField(max_length=254, primary_key=True, serialize=False),
        ),
    ]
