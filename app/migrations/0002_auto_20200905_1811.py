# Generated by Django 3.1.1 on 2020-09-05 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='algorithm',
            old_name='title',
            new_name='name',
        ),
        migrations.AddField(
            model_name='algorithm',
            name='slug',
            field=models.SlugField(default='halo', unique=True),
            preserve_default=False,
        ),
    ]
