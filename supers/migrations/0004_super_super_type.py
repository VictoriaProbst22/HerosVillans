# Generated by Django 4.0.4 on 2022-05-26 21:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('super_types', '0001_initial'),
        ('supers', '0003_remove_super_super_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='super',
            name='super_type',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='super_types.super_types'),
        ),
    ]
