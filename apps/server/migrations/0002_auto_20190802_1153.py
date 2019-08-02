# Generated by Django 2.1.5 on 2019-08-02 03:53

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('server', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Radiusban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户')),
            ],
        ),
        migrations.CreateModel(
            name='Relay',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('port', models.CharField(max_length=30, verbose_name='端口')),
                ('priority', models.CharField(choices=[('0', '优先'), ('1', '不优先')], default='0', max_length=30, verbose_name='优先级')),
            ],
        ),
        migrations.CreateModel(
            name='Serveronlinelog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('online_user', models.IntegerField(verbose_name='在线用户')),
                ('log_time', models.DateTimeField(auto_now_add=True, verbose_name='记录时间')),
            ],
        ),
        migrations.CreateModel(
            name='Speedtest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('telecomeping', models.TextField(verbose_name='电信ping')),
                ('telecomeupload', models.TextField(verbose_name='电信upload')),
                ('telecomedownload', models.TextField(verbose_name='电信download')),
                ('unicomping', models.TextField(verbose_name='联通ping')),
                ('unicomupload', models.TextField(verbose_name='联通upload')),
                ('unicomdownload', models.TextField(verbose_name='联通download')),
                ('cmccping', models.TextField(verbose_name='移动ping')),
                ('cmccupload', models.TextField(verbose_name='移动upload')),
                ('cmccdownload', models.TextField(verbose_name='移动download')),
            ],
        ),
        migrations.CreateModel(
            name='Unblockip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateField(auto_created=True, verbose_name='创建时间')),
                ('ip', models.GenericIPAddressField()),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户 ')),
            ],
        ),
        migrations.DeleteModel(
            name='Node',
        ),
        migrations.RemoveField(
            model_name='serverinfo',
            name='ip',
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='bandwidthlimit_resetday',
            field=models.IntegerField(null=True, verbose_name='带宽重置日'),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='info',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='备注'),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='node_bandwidth',
            field=models.BigIntegerField(null=True, verbose_name='带宽'),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='node_bandwidth_limit',
            field=models.BigIntegerField(null=True, verbose_name='带宽限制'),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='node_connector',
            field=models.IntegerField(null=True, verbose_name='连接数'),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='node_group',
            field=models.IntegerField(null=True, verbose_name='组'),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='node_speedlimit',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=12, verbose_name='节点限速'),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='server',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='地址'),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='status',
            field=models.CharField(choices=[('0', '可用'), ('1', '不可用')], default='0', max_length=30, verbose_name='节点状态'),
        ),
        migrations.AddField(
            model_name='serverinfo',
            name='traffic_rate',
            field=models.CharField(max_length=30, null=True, verbose_name='流量比率'),
        ),
        migrations.AlterField(
            model_name='aliveip',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.Serverinfo', verbose_name='节点 '),
        ),
        migrations.AlterField(
            model_name='blockip',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.Serverinfo', verbose_name='节点 '),
        ),
        migrations.AddField(
            model_name='speedtest',
            name='node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.Serverinfo', verbose_name='节点'),
        ),
        migrations.AddField(
            model_name='serveronlinelog',
            name='server',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='server.Serverinfo', verbose_name='服务'),
        ),
        migrations.AddField(
            model_name='relay',
            name='dist_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='dist_node', to='server.Serverinfo', verbose_name='目标节点'),
        ),
        migrations.AddField(
            model_name='relay',
            name='source_node',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='source_node', to='server.Serverinfo', verbose_name='源节点'),
        ),
        migrations.AddField(
            model_name='relay',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='用户'),
        ),
    ]