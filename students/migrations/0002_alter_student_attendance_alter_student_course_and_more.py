# Generated by Django 4.2.9 on 2024-02-06 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='attendance',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=13),
        ),
        migrations.AlterField(
            model_name='student',
            name='course',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='date_time',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='name',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='student',
            name='room',
            field=models.DecimalField(decimal_places=0, default=0, max_digits=20),
        ),
        migrations.AlterField(
            model_name='student',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]