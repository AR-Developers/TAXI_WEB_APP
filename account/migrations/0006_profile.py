# Generated by Django 3.1.6 on 2021-02-16 16:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0005_auto_20210214_0711'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('org_name', models.CharField(max_length=256)),
                ('ven_name', models.CharField(max_length=256)),
                ('ven_email', models.EmailField(max_length=256, unique=True)),
                ('ven_phone', models.IntegerField()),
                ('add', models.TextField()),
                ('state', models.CharField(max_length=256)),
                ('city', models.CharField(max_length=256)),
                ('pincode', models.IntegerField()),
                ('lat', models.DecimalField(blank=True, decimal_places=10, max_digits=40, null=True)),
                ('lon', models.DecimalField(blank=True, decimal_places=10, max_digits=40, null=True)),
                ('value', models.BooleanField(default=False)),
                ('is_paid', models.BooleanField(default=False)),
                ('updated_on', models.DateTimeField(auto_now=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]