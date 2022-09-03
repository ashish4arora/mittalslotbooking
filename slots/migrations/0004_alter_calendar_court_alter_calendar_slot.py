# Generated by Django 4.1 on 2022-08-27 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_alter_courts_sport'),
        ('slots', '0003_remove_calendar_court_calendar_court'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='court',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='calendar', to='courts.courts'),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='slot',
            field=models.ManyToManyField(related_name='calendar', to='slots.slots'),
        ),
    ]
