# Generated by Django 5.1.1 on 2024-09-09 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('mobile_number', models.CharField(max_length=15)),
            ],
        ),
    ]
