# Generated by Django 3.0.5 on 2020-05-18 09:20

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('drishya', '0008_payment'),
    ]

    operations = [
        migrations.AddField(
            model_name='images2',
            name='profile_pic',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='images/'),
            preserve_default=False,
        ),
    ]