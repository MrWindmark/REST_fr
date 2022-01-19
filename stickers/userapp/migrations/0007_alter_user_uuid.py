# Generated by Django 4.0 on 2022-01-19 19:32

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0006_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('22720d73-e7b0-4f5a-8d91-151f6f249431'), primary_key=True, serialize=False),
        ),
    ]