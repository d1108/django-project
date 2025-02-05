# Generated by Django 3.0.5 on 2020-05-18 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drishya', '0009_images2_profile_pic'),
    ]

    operations = [
        migrations.CreateModel(
            name='newpost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('img', models.ImageField(upload_to='images/')),
                ('caption', models.TextField()),
                ('price', models.IntegerField()),
                ('likes', models.IntegerField()),
                ('purchased', models.CharField(max_length=20)),
                ('mobile_no', models.IntegerField()),
                ('profile_pic', models.ImageField(upload_to='images/')),
            ],
        ),
    ]
