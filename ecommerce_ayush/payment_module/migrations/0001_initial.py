# Generated by Django 3.1.1 on 2020-11-26 00:58

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentGateway',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('token', models.UUIDField(default=uuid.uuid4, editable=False)),
                ('expiry_date', models.DateField()),
                ('balance', models.FloatField()),
                ('is_active', models.BooleanField()),
            ],
        ),
    ]
