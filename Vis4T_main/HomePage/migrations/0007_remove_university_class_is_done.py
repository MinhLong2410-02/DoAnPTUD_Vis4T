# Generated by Django 4.1.7 on 2023-05-24 13:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('HomePage', '0006_remove_teacher_is_done_adding_class_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='university_class',
            name='is_done',
        ),
    ]
