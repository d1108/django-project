# Generated by Django 3.0.5 on 2020-05-15 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drishya', '0005_addimages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mobile_no', models.IntegerField()),
                ('img', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
