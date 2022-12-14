# Generated by Django 4.1 on 2022-08-26 20:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_alter_courts_sport'),
        ('slots', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Days',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('day', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Calendar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(blank=True, null=True)),
                ('court', models.ManyToManyField(related_name='calender', to='courts.courts')),
                ('day', models.ManyToManyField(related_name='calendar', to='slots.days')),
                ('slot', models.ManyToManyField(related_name='calender', to='slots.slots')),
            ],
        ),
    ]
