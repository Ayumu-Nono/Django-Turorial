# Generated by Django 2.2.3 on 2019-07-20 06:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Memos',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('title', models.TextField(max_length=20)),
                ('sammary', models.TextField(max_length=100)),
                ('slogan', models.TextField(max_length=20)),
                ('fact', models.TextField(max_length=100)),
                ('abstraction', models.TextField(max_length=100)),
                ('diverse', models.TextField(max_length=100)),
            ],
        ),
    ]
