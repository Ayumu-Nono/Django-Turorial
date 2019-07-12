# Generated by Django 2.2.2 on 2019-07-12 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0002_auto_20190710_0624'),
    ]

    operations = [
        migrations.CreateModel(
            name='DonorSearch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('family_name', models.CharField(max_length=20)),
                ('first_name', models.CharField(max_length=20)),
                ('blood_type', models.CharField(max_length=5)),
                ('birth_place', models.CharField(max_length=20)),
                ('memo', models.TextField(max_length=200)),
            ],
        ),
    ]
