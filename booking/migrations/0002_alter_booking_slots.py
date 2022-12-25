# Generated by Django 3.2.16 on 2022-12-25 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='slots',
            field=models.IntegerField(choices=[(15, '15:00'), (10, '10:00'), (17, '17:00'), (11, '11:00'), (18, '18:00'), (12, '12:00'), (13, '13:00'), (14, '14:00'), (16, '16:00')], default='10'),
        ),
    ]
