# Generated by Django 4.2.11 on 2024-05-30 13:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0005_employee_can_manage_participants'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='can_manage_participants',
            field=models.BooleanField(default=True),
        ),
    ]
