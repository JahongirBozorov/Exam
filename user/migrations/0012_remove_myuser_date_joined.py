# Generated by Django 4.2.9 on 2024-01-25 07:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_alter_myuser_date_joined'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='myuser',
            name='date_joined',
        ),
    ]
