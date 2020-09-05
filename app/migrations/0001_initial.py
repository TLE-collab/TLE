# Generated by Django 3.1.1 on 2020-09-05 14:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Algorithm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=68, unique=True)),
                ('description', models.CharField(max_length=1000)),
                ('solution', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=68, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
