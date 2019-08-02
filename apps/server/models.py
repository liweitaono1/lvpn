from django.db import models

# Create your models here.
from users.models import User

SERVERTYPE = (
    (str(0), u"独立服务器"),
    (str(1), u"场控制器服务器"),
    (str(2), u"场成员服务器"),
)
SERVERSTATUS = (
    (str(0), u"可用"),
    (str(1), u"不可用"),
)
RELAY_PRIORITY = (
    (str(0), u"优先"),
    (str(1), u"不优先"),
)


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Serverinfo(models.Model):
    server = models.CharField(verbose_name=u"地址", max_length=100, unique=True, null=True)
    name = models.CharField(verbose_name=u"服务器名", max_length=30)
    hub = models.CharField(verbose_name=u'HUBNAME', max_length=100)
    password = models.CharField(verbose_name=u'密码', max_length=255)
    type = models.CharField(verbose_name=u'类型', choices=SERVERTYPE, null=True, max_length=30)
    status = models.CharField(verbose_name=u'节点状态', choices=SERVERSTATUS, max_length=30, default='0')
    traffic_rate = models.CharField(verbose_name=u'流量比率', max_length=30, null=True)
    node_speedlimit = models.DecimalField(verbose_name=u'节点限速', decimal_places=2, max_digits=12, default=0.00)
    node_connector = models.IntegerField(verbose_name=u'连接数', null=True)
    node_bandwidth = models.BigIntegerField(verbose_name=u'带宽', null=True)
    node_bandwidth_limit = models.BigIntegerField(verbose_name=u'带宽限制', null=True)
    bandwidthlimit_resetday = models.IntegerField(verbose_name=u'带宽重置日', null=True)
    node_group = models.IntegerField(verbose_name=u'组', null=True)
    info = models.CharField(verbose_name=u'备注', max_length=100, blank=True, null=True)

    def __unicode__(self):
        return


class Serveronlinelog(models.Model):
    server = models.ForeignKey(Serverinfo, on_delete=models.SET_NULL, verbose_name=u'服务', null=True)
    online_user = models.IntegerField(verbose_name=u'在线用户')
    log_time = models.DateTimeField(auto_now_add=True, verbose_name=u'记录时间')

    def __unicode__(self):
        return


class Aliveip(models.Model):
    node = models.ForeignKey(Serverinfo, verbose_name=u'节点 ', on_delete=models.SET_NULL, null=True)
    ip = models.GenericIPAddressField()

    def __unicode__(self):
        return


class Blockip(models.Model):
    node = models.ForeignKey(Serverinfo, verbose_name=u'节点 ', on_delete=models.SET_NULL, null=True)
    ip = models.GenericIPAddressField()
    datetime = models.DateField(verbose_name=u'创建时间', auto_created=True)

    def __unicode__(self):
        return


class Unblockip(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户 ', on_delete=models.SET_NULL, null=True)
    ip = models.GenericIPAddressField()
    datetime = models.DateField(verbose_name=u'创建时间', auto_created=True)

    def __unicode__(self):
        return


class Relay(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name=u'用户', null=True)
    source_node = models.ForeignKey(Serverinfo, related_name='source_node', on_delete=models.SET_NULL,
                                    verbose_name=u'源节点', null=True)
    dist_node = models.ForeignKey(Serverinfo, related_name='dist_node', on_delete=models.SET_NULL, verbose_name=u'目标节点',
                                  null=True)
    port = models.CharField(verbose_name=u'端口', max_length=30)
    priority = models.CharField(verbose_name=u'优先级', choices=RELAY_PRIORITY, max_length=30, default='0')

    def __unicode__(self):
        return


class Speedtest(models.Model):
    node = models.ForeignKey(Serverinfo, on_delete=models.SET_NULL, verbose_name=u'节点', null=True)
    datetime = models.DateTimeField(auto_now_add=True)
    telecomeping = models.TextField(verbose_name=u'电信ping')
    telecomeupload = models.TextField(verbose_name=u'电信upload')
    telecomedownload = models.TextField(verbose_name=u'电信download')
    unicomping = models.TextField(verbose_name=u'联通ping')
    unicomupload = models.TextField(verbose_name=u'联通upload')
    unicomdownload = models.TextField(verbose_name=u'联通download')
    cmccping = models.TextField(verbose_name=u'移动ping')
    cmccupload = models.TextField(verbose_name=u'移动upload')
    cmccdownload = models.TextField(verbose_name=u'移动download')

    def __unicode__(self):
        return self.node.name


class Radiusban(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, verbose_name=u'用户', null=True)

    def __unicode__(self):
        return self.user.name
