# Generated by Django 3.1.6 on 2021-02-14 07:11

import account.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20210214_0632'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendoraccount',
            name='created_by',
            field=models.ForeignKey(blank=True, default=account.models.Account, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
