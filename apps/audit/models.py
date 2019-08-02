from django.db import models

# Create your models here.
from goods.models import Shop
from server.models import Serverinfo
from users.models import User

DETECT_TYPE = (
    (str(0), u"明文匹配"),
    (str(1), u"hex匹配"),
)


class Recharge(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户', on_delete=models.PROTECT)
    shop = models.ForeignKey(Shop, verbose_name=u'商品', on_delete=models.PROTECT)
    datetime = models.DateTimeField(verbose_name=u'创建时间', auto_created=True)
    renew = models.CharField(u'自动续费时间', max_length=128)
    coupon = models.CharField(verbose_name=u'优惠券', max_length=128)
    price = models.DecimalField(verbose_name=u'金额', decimal_places=2, max_digits=10)

    def __unicode__(self):
        if hasattr(self.user, 'name'):
            return self.user.name
        return self.datetime


class Analysis(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户', on_delete=models.PROTECT)
    ip = models.GenericIPAddressField(verbose_name=u'登录ip')
    datetime = models.DateTimeField(verbose_name=u'时间', auto_now_add=True)
    type = models.CharField(verbose_name=u'类型', max_length=32, default='1')

    def __unicode__(self):
        if hasattr(self.user, 'name'):
            return self.user.name
        else:
            return self.ip


class Detectlist(models.Model):
    name = models.CharField(verbose_name=u'名称', max_length=30)
    text = models.TextField(verbose_name=u'文本')
    regex = models.CharField(verbose_name=u'正则表达式规则', max_length=100)
    type = models.CharField(verbose_name=u'类型', choices=DETECT_TYPE, max_length=30)

    def __unicode__(self):
        return self.name


class Detectlog(models.Model):
    datetime = models.DateTimeField(verbose_name=u'时间', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=u'用户', on_delete=models.SET_NULL, null=True)
    list = models.ForeignKey(Detectlist, verbose_name=u'列表', on_delete=models.SET_NULL,null=True)
    node = models.ForeignKey(Serverinfo, verbose_name=u'节点', on_delete=models.SET_NULL,null=True)

    def __unicode__(self):
        if hasattr(self.user, 'name'):
            return self.user.name
        else:
            return self.datetime


class Usertrafficlog(models.Model):
    user = models.ForeignKey(User, verbose_name=u'用户', on_delete=models.SET_NULL,null=True)
    node = models.ForeignKey(Serverinfo, verbose_name=u'节点', on_delete=models.SET_NULL,null=True)
    rate = models.IntegerField(verbose_name=u'速率')
    traffic = models.IntegerField(verbose_name=u'流量')
    log_time = models.DateTimeField(auto_now_add=True)


class Login(models.Model):
    datetime = models.DateTimeField(verbose_name=u'时间', auto_now_add=True)
    user = models.ForeignKey(User, verbose_name=u'用户', on_delete=models.SET_NULL,null=True)
    ip = models.GenericIPAddressField(verbose_name=u'登录ip')
    type = models.CharField(verbose_name=u'类型',max_length=30)

    def __unicode__(self):
        if hasattr(self.user, 'name'):
            return self.user.name
        else:
            return self.datetime
