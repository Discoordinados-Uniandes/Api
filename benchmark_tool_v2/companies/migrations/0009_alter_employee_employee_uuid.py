# Generated by Django 5.0.6 on 2024-05-11 10:16

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('companies', '0008_remove_employee_employee_id_employee_employee_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='employee_uuid',
            field=models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
