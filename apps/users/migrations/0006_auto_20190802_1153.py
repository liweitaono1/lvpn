# Generated by Django 2.1.5 on 2019-08-02 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_invite_code'),
    ]

    operations = [
        migrations.AlterField(
            model_name='invite_code',
            name='create_time',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='invite_code',
            name='update_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
