# Generated by Django 2.2 on 2019-04-02 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('index', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='login',
            name='roll_number',
            field=models.IntegerField(),
        ),
    ]
