# Generated by Django 4.2.11 on 2024-05-15 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Employee', '0004_alter_employee_position'),
    ]

    operations = [
        migrations.AddField(
            model_name='employee',
            name='can_manage_participants',
            field=models.BooleanField(default=False),
        ),
    ]