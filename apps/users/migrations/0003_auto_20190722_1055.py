# Generated by Django 2.1.5 on 2019-07-22 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_auto_20190722_1047'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='communication_account',
            field=models.CharField(max_length=128, null=True, verbose_name='通信账号'),
        ),
        migrations.AddField(
            model_name='user',
            name='communication_mode',
            field=models.CharField(choices=[('1', '微信'), ('2', 'QQ'), ('3', 'Facebook'), ('4', 'Telegram')], max_length=32, null=True, verbose_name='通信方式'),
        ),
        migrations.AlterField(
            model_name='user',
            name='create_time',
            field=models.DateTimeField(auto_created=True, verbose_name='创建时间'),
        ),
    ]
