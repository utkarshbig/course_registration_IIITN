# Generated by Django 4.2.6 on 2024-02-16 16:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_alter_semester_info_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='semester_info',
            name='user',
        ),
    ]
