import random
import re

import qrcode as qrcode
from django.contrib.auth import logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import check_password
from django.db.models import Q
from django.http import HttpResponse
from django.shortcuts import redirect
# Create your views here.
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.generics import CreateAPIView
from rest_framework.response import Response
from six import BytesIO

from audit.models import Analysis
from lvpn.settings import conn
from lvpn.throttles import LoginRateThrottle, RegistRateThrottle
from users import serializers
from users.models import User
from users.tasks import send_token, test
from utils.captcha.pic_captcha import captcha
from utils.checkUserName import check_user_name


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Vpnuser(request):
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass


@throttle_classes([LoginRateThrottle])
class UserView(CreateAPIView):
    serializer_class = serializers.CreateUserSerializer


@throttle_classes([LoginRateThrottle])
@api_view(['POST'])
def Login(request):
    res = {'code': 0, 'msg': "", 'data': ''}
    username = request.data.get("username")  # 获取用户名
    password = request.data.get("password")  # 获取用户的密码
    try:
        user = User.objects.get(Q(username=username) | Q(email=username))
        if check_password(password, user.password):
            if user.status == True:
                login(request, user)  # 用户登陆
                res['code'] = 0
                res['msg'] = '登录成功'
            else:
                res['code'] = 1
                res['msg'] = '用户未激活'
        else:
            res['code'] = 1
            res['msg'] = '用户名或密码错误'

    except Exception as e:
        res['code'] = 1
        res['msg'] = '用户名或密码错误'

    return Response(res)


@login_required
@api_view(['GET'])
def Logout(request):
    try:
        logout(request)
        Analysis.objects.create(user=request.user, ip=request.META['remote_ip'], type=2)
    except Exception as e:
        print(e)
    return redirect('Login')


@throttle_classes([RegistRateThrottle])
@api_view(['POST'])
def Regist(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    data = request.data.copy()
    token = data.pop('token')
    email = data.get('email')
    email_code = conn.get("email_code_id_" + email)
    if all([email, email_code, token]):
        if token != email_code.decode('utf-8'):
            return Response({'code': 1, 'msg': '参数不足', 'data': ''})
    else:
        return Response({'code': 1, 'msg': '参数不足', 'data': ''})
    try:
        User.objects.create(data)
        res['msg'] = '创建成功'
    except Exception as e:
        res['code'] = 1
        res['msg'] = '创建失败'
        print(e)
    return Response(res)


@throttle_classes([RegistRateThrottle])
@api_view(['POST'])
def get_img_code(request):
    # 获取图片验证码
    img_code_id = request.data.get("img_code_id")

    # 校验参数
    if not img_code_id:
        return Response(403)  # 拒绝访问

    # 生成图片验证码
    img_name, img_text, img_bytes = captcha.generate_captcha()

    # 保存验证码文字和图片key  redis  设置过期时间
    try:
        conn.set("img_code_id_" + img_code_id, img_text, ex=300)
    except BaseException as e:
        print(e)  # 记录错误信息
        return Response(404)

    return HttpResponse(img_bytes, content_type="image/jpeg")


@api_view(['POST'])
def generate_token(request):
    # 生成邮箱校验码
    res = {'code': 0, 'msg': '', 'data': ''}
    img_code_id = request.data.get("img_code_id")
    img_code = request.data.get("img_code")
    email = request.data.get("email")
    if not all([img_code_id, img_code, email]):
        res['code'] = 1
        res['msg'] = '参数不足'
    else:
        if not re.match(r"^[a-zA-Z0-9_-]+@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+)+$", email):
            res['code'] = 1
            res['msg'] = '参数异常'
            return Response(res)

        # 校验图片验证码  根据图片key取出真实的验证码文字
        real_img_code = conn.get("img_code_id_" + img_code_id)
        if real_img_code is None:
            res['code'] = 1
            res['msg'] = '参数异常'
            return Response(res)

        if real_img_code.decode('utf-8') != img_code.upper():
            res['code'] = 1
            res['msg'] = '参数异常'
            return Response(res)
        # 判断用户是否存在
        try:
            User.objects.get(email=email)
            res['code'] = 1
            res['msg'] = '用户已存在'
            return Response(res)
        except Exception as e:
            pass
        # 生成随机短信验证码
        rand_num = "%04d" % random.randint(0, 9999)
        # 打印验证码
        print("邮箱验证码为:%s" % rand_num)
        conn.set("email_code_id_" + email, rand_num, ex=300)

        res = send_token(to_email=email, token=rand_num)
        if res:
            res['msg'] = '成功'
        else:
            res['code'] = 1
            res['msg'] = '失败'

    return Response(res)


@api_view(['POST'])
def generate_qrcode(request):
    # 生成二维码
    img = qrcode.make(request.data)
    buf = BytesIO()
    img.save(buf)
    image_stream = buf.getvalue()
    return Response(image_stream)
