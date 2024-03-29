# Generated by Django 4.2.9 on 2024-01-25 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_myuser_is_staff'),
    ]

    operations = [
        migrations.AddField(
            model_name='myuser',
            name='date_joined',
            field=models.DateTimeField(default=None),
        ),
        migrations.AddField(
            model_name='myuser',
            name='is_active',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='is_staff',
            field=models.IntegerField(default=False),
        ),
        migrations.AlterModelTable(
            name='myuser',
            table='auth_user',
        ),
    ]
