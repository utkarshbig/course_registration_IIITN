# Generated by Django 4.2.6 on 2024-02-18 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0012_rename_course_name_group_course_name1_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_info',
            name='groups',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='home.group'),
        ),
    ]
