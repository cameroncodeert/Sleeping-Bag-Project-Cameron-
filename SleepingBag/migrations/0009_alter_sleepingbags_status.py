# Generated by Django 4.2.11 on 2024-05-31 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SleepingBag', '0008_alter_sleepingbags_date_of_received_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sleepingbags',
            name='status',
            field=models.CharField(choices=[('Good', 'Goed'), ('Damaged', 'Beschadigd'), ('Lost', 'Verloren')], max_length=10, verbose_name='Status'),
        ),
    ]