# Generated by Django 3.1.1 on 2020-09-08 12:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='playstore',
            name='slug',
            field=models.CharField(default='', max_length=121),
            preserve_default=False,
        ),
    ]
