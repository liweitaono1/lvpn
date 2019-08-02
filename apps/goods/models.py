from django.db import models

# Create your models here.
GOODS_STATUS = (
    (str(0), u"上架"),
    (str(1), u"下架"),
    (str(2), u"创建"),
    (str(3), u"删除"),
)


class Shop(models.Model):
    name = models.CharField(verbose_name=u'商品名', max_length=128)
    price = models.DecimalField(verbose_name=u'价格', decimal_places=2, max_digits=10)
    content = models.TextField(verbose_name=u'内容')
    auto_renew = models.BooleanField(verbose_name=u'自动续费')
    auto_reset_bandwidth = models.BooleanField(verbose_name=u'自动重置带宽')
    status = models.CharField(verbose_name=u'商品状态', choices=GOODS_STATUS, max_length=32)

    def __unicode__(self):
        return self.name

