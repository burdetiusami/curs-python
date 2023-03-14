# Generated by Django 4.1.7 on 2023-03-14 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=80)),
                ('address', models.CharField(max_length=80)),
                ('cargo_info', models.CharField(max_length=100)),
                ('eta', models.DateField()),
                ('status', models.BooleanField(default=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
