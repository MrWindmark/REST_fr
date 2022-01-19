# Generated by Django 4.0 on 2022-01-19 19:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('userapp', '0008_alter_user_uuid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='uuid',
            field=models.UUIDField(default=uuid.UUID('ea3b8b43-db9e-473a-ac7b-e35c41a36133'), primary_key=True, serialize=False),
        ),
    ]
