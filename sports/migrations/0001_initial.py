# Generated by Django 4.1 on 2022-08-23 13:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sports',
            fields=[
                ('sportid', models.CharField(max_length=3, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=25)),
            ],
        ),
    ]
