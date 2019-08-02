from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
from goods.models import Shop

USER_STATUS = (
    (str(1), u"激活"),
    (str(2), u"未激活"),
    (str(3), u"过期"),
    (str(4), u"注销"),
)

COMMUNICATION_MODE = (
    (str(1), u"微信"),
    (str(2), u"QQ"),
    (str(3), u"Facebook"),
    (str(4), u"Telegram"),
)


class User(AbstractUser):
    name = models.CharField(verbose_name=u'用户名', max_length=128, blank=True)
    password = models.CharField(verbose_name=u'密码', max_length=256, blank=True)
    token = models.CharField(verbose_name=u'令牌', max_length=32, blank=True)
    email = models.EmailField(verbose_name=u'邮箱', max_length=32, blank=True)
    # node_group = models.ForeignKey(verbose_name=u"节点组", on_delete=models.SET_NULL,)
    port = models.CharField(verbose_name=u'端口', max_length=16, blank=True)
    money = models.CharField(verbose_name=u'重置总金额', max_length=256, blank=True)
    create_time = models.DateTimeField(verbose_name=u'创建时间', auto_created=True)
    expire_time = models.DateTimeField(verbose_name=u'过期时间', auto_now=True)
    status = models.CharField(verbose_name=u"用户状态", choices=USER_STATUS, max_length=32, default='2')
    inviter = models.ForeignKey('self', verbose_name=u"邀请人", on_delete=models.SET_NULL, null=True)
    check_in_time = models.DateTimeField(verbose_name=u'最后签到时间', auto_now=True)
    is_admin = models.BooleanField(verbose_name=u'是否是管理员', default=False)
    communication_mode = models.CharField(verbose_name=u'通信方式', choices=COMMUNICATION_MODE, max_length=32, null=True)
    communication_account = models.CharField(verbose_name=u'通信账号', max_length=128, null=True)

    def __unicode__(self):
        return self.name


class Coupon(models.Model):
    name = models.CharField(verbose_name=u'优惠券名', max_length=128)
    code = models.CharField(verbose_name=u'优惠码', max_length=256)
    expire = models.CharField(verbose_name=u'过期时间', max_length=128)

    shop = models.ForeignKey(Shop, verbose_name=u'商品', on_delete=models.SET_NULL, null=True)

    def __unicode__(self):
        return self.name


from server.models import BaseModel


class Invite_code(BaseModel):
    code = models.CharField(verbose_name=u'邀请码', max_length=128, blank=False)
    user = models.ForeignKey(User, verbose_name=u'用户', on_delete=models.CASCADE, blank=False)

    def __unicode__(self):
        return self.code


class Link(models.Model):
    type = models.CharField(verbose_name=u'类型')
    address = models.CharField(verbose_name=u'地址')
    port = models.CharField(verbose_name=u'端口')
    token = models.CharField(verbose_name=u'token')
    ios = models.CharField(verbose_name=u'ios')
    user = models.ForeignKey(User, verbose_name=u'用户', on_delete=models.SET_NULL)
    isp = models.CharField()
    geo = models.CharField()
    method = models.CharField()

    def __unicode__(self):
        return self.address

    class Meta:
        abstract = True
