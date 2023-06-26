# Generated by Django 4.2.1 on 2023-06-25 21:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0010_alter_revoke_code'),
        ('dashboard', '0010_alter_medicalhistory_doctor_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='account.patient'),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_mdoctor', to='account.doctor'),
        ),
        migrations.AlterField(
            model_name='medicalhistory',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='patient_mhistory', to='account.patient'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_prescription', to='account.doctor'),
        ),
        migrations.AlterField(
            model_name='prescription',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_prescription', to='account.patient'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='doctor',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='doctor_rate', to='account.doctor'),
        ),
        migrations.AlterField(
            model_name='rate',
            name='patient',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='user_rate', to='account.patient'),
        ),
    ]
