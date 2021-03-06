# Generated by Django 2.2.4 on 2019-09-27 05:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('backend_main', '0002_auto_20190601_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='MedicineSellModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coustomer_contact', models.CharField(max_length=20)),
                ('medicine_buy_date', models.DateTimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('coustomer_name', models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='backend_main.PatientModel')),
            ],
        ),
        migrations.CreateModel(
            name='SellDetialsModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medicine_name', models.CharField(max_length=50)),
                ('total_course', models.CharField(max_length=100)),
                ('total_buy', models.CharField(max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(verbose_name=True)),
                ('deleted_at', models.DateTimeField(blank=True, null=True)),
                ('medicine_sell_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='backend_main.MedicineSellModel')),
            ],
        ),
    ]
