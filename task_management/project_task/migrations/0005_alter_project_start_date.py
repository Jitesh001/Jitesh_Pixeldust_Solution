# Generated by Django 5.0.6 on 2024-05-21 17:32

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project_task', '0004_alter_project_description_alter_task_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='start_date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
