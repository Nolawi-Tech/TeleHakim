# Generated by Django 4.2.1 on 2023-06-25 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appointment', '0011_appadmin_attendee_appadmin_host_appointment_attendee_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='appadmin',
            name='room_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='appointment',
            name='room_id',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
