# Generated by Django 3.2.9 on 2022-11-13 19:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_follow'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='follow',
        ),
    ]
