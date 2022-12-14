# Generated by Django 4.1 on 2022-08-23 13:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('courts', '0001_initial'),
        ('sports', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemname', models.CharField(max_length=25)),
                ('court', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='courts.courts')),
                ('sportid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inventory', to='sports.sports')),
            ],
        ),
    ]
