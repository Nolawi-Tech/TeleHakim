# Generated by Django 4.2.1 on 2023-06-22 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0005_alter_appointment_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='appointment',
            name='is_notified',
            field=models.BooleanField(default=False),
        ),
    ]