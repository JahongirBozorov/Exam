# Generated by Django 4.2.9 on 2024-02-09 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0002_teacher_room_alter_teacher_img_alter_teacher_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='room',
            field=models.IntegerField(default=1),
        ),
    ]
