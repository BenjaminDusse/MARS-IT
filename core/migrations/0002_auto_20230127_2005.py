# Generated by Django 3.2.4 on 2023-01-27 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='chat_id',
            field=models.PositiveBigIntegerField(null=True, unique=True),
        ),
        migrations.AddField(
            model_name='customuser',
            name='tg_user_id',
            field=models.PositiveBigIntegerField(null=True, unique=True),
        ),
    ]
