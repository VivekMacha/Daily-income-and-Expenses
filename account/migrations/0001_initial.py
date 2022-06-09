# Generated by Django 3.2.7 on 2022-02-16 06:07

import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='auth.user')),
                ('age', models.IntegerField()),
                ('gender', models.CharField(max_length=10)),
                ('contact', models.CharField(max_length=15)),
                ('address', models.TextField(max_length=300)),
            ],
            options={
                'db_table': 'user_info',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
    ]