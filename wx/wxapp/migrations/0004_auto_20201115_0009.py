# Generated by Django 3.0.6 on 2020-11-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0003_token_token'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='token',
            field=models.CharField(max_length=50),
        ),
    ]