# Generated by Django 4.1.4 on 2023-01-22 08:27

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chatuser_date_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chatuser',
            name='date_created',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 22, 8, 27, 55, 390)),
        ),
    ]
