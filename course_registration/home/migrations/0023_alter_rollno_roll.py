# Generated by Django 4.2.6 on 2024-02-19 13:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0022_remove_semester_info_rolls'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rollno',
            name='roll',
            field=models.CharField(max_length=100),
        ),
    ]
