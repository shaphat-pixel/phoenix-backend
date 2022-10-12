# Generated by Django 4.0 on 2022-10-12 16:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('Phone_Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Citizen',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_of_citizen', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('sex', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('date_of_birth', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('place_of_birth', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('gps_address', models.CharField(blank=True, default='', max_length=300, null=True)),
                ('phone_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Phone_Book.phonebook')),
            ],
        ),
    ]
