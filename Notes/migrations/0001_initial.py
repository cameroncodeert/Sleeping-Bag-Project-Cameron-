# Generated by Django 4.2.11 on 2024-04-30 11:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.TextField(max_length=500)),
                ('date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]