# Generated by Django 3.2.25 on 2024-09-09 05:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_program'),
    ]

    operations = [
        migrations.AlterField(
            model_name='program',
            name='schedule',
            field=models.DateTimeField(auto_now=True),
        ),
    ]