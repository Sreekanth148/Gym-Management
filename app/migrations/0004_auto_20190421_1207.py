# Generated by Django 2.1.7 on 2019-04-21 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_add_fee_deatails_add_gym_center_details_add_trainee_details'),
    ]

    operations = [
        migrations.AlterField(
            model_name='add_gym_center_details',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='add_trainee_details',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
