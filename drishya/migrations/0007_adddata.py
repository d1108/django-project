# Generated by Django 3.0.5 on 2020-05-17 06:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drishya', '0006_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Adddata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('img_id', models.IntegerField()),
            ],
        ),
    ]
