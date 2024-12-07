# Generated by Django 5.1.4 on 2024-12-05 07:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('quantity', models.IntegerField(default=0)),
                ('price', models.FloatField(default=0.0)),
                ('category', models.CharField(max_length=200)),
                ('deactivation_date', models.DateTimeField(default=None)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('is_admin', models.BooleanField(default=False)),
            ],
        ),
    ]
