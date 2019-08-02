# 自定义jwt认证成功返回的数据 ==> 用户登录成功返回的数据
import re

from django.contrib.auth.backends import ModelBackend

# 用户名或者工号登录
from users.models import User


def get_user_by_account(account):
    """
    根据帐号获取user对象
    :param account: 账号，可以是用户名，也可以是手机号
    :return: User对象 或者 None
    """
    try:
        if re.match(r'(\d+|\w+\d+)', account):
            # 帐号为手机号
            user = User.objects.get(jobnumber=account)
        else:
            # 帐号为用户名
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:
        return user


def jwt_response_payload_handler(token, user=None, request=None):
    return {
        'token': token,
        'user_id': user.id,
        'username': user.username
    }


class UsernameMobileAuthBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        # 在这里使用上面自定义的获取用户信息方法, 拿到用户后校验jwt
        user = get_user_by_account(username)
        if user is not None and user.check_password(password):
            return user
