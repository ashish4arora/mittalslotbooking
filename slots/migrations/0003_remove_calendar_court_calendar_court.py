# Generated by Django 4.1 on 2022-08-26 20:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0002_alter_courts_sport'),
        ('slots', '0002_days_calendar'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='calendar',
            name='court',
        ),
        migrations.AddField(
            model_name='calendar',
            name='court',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='calender', to='courts.courts'),
            preserve_default=False,
        ),
    ]
