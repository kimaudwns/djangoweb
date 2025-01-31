# Generated by Django 3.2.25 on 2024-09-09 05:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Program',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('subtext', models.TextField()),
                ('schedule', models.TextField()),
                ('img', models.ImageField(blank=True, upload_to='img')),
            ],
        ),
    ]
