# Generated by Django 3.0.6 on 2020-11-24 14:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wxapp', '0011_likecats_likecomments_likeposts'),
    ]

    operations = [
        migrations.AddField(
            model_name='cats',
            name='urllist',
            field=models.CharField(default='', max_length=2000),
        ),
    ]
