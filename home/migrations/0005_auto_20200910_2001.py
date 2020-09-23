# Generated by Django 3.1.1 on 2020-09-10 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_donate'),
    ]

    operations = [
        migrations.AddField(
            model_name='donate',
            name='amount',
            field=models.CharField(default='', max_length=11),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='donate',
            name='email',
            field=models.EmailField(default='', max_length=254),
            preserve_default=False,
        ),
    ]