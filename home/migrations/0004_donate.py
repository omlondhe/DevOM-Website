# Generated by Django 3.1.1 on 2020-09-10 12:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_auto_20200908_1449'),
    ]

    operations = [
        migrations.CreateModel(
            name='Donate',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=251)),
                ('last_name', models.CharField(max_length=251)),
                ('description', models.TextField()),
            ],
        ),
    ]