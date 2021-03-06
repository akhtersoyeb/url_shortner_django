# Generated by Django 3.1.5 on 2021-01-11 13:57

from django.db import migrations, models
import urlshortner.models


class Migration(migrations.Migration):

    dependencies = [
        ('urlshortner', '0002_auto_20210106_1654'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='short_url',
            field=models.CharField(default=urlshortner.models.generate_random_code, max_length=8, unique=True),
        ),
    ]
