# Generated by Django 3.1.1 on 2020-09-08 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayStore',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=251)),
                ('description', models.TextField()),
                ('timestamp', models.DateTimeField(blank=True)),
            ],
        ),
    ]