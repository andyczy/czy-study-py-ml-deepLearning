# Generated by Django 2.1.3 on 2018-11-12 06:09

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.CharField(max_length=32, primary_key=True, serialize=False)),
                ('userName', models.CharField(max_length=32)),
            ],
        ),
    ]
