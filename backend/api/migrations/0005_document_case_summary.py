# Generated by Django 5.2 on 2025-04-23 14:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_user_role'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='case_summary',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='api.casesummary'),
            preserve_default=False,
        ),
    ]
