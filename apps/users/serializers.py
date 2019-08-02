import re
from .models import User
from rest_framework import serializers
from rest_framework_jwt.settings import api_settings


# 创建用户
class CreateUserSerializer(serializers.ModelSerializer):
    # ModelSerializer ==> 模型类序列化器(校验用户提交的数据)
    # 用户注册
    """
    提交字段
    1. username
    2. password
    3. password2
    4. mobile
    5. email_code
    6. allow
    返回字段
    1. id
    2. username
    3. mobile
    4. jwt token
    """
    password2 = serializers.CharField(label='确认密码', write_only=True)
    allow = serializers.CharField(label='是否同意协议', write_only=True)
    token = serializers.CharField(label='token', read_only=True)

    class Meta:
        # 指明参照哪个模型类
        model = User
        # 指明为模型类的哪些字段生成
        fields = ['id', 'jobnumber', 'username', 'mobile', 'password', 'password2', 'allow', 'token']

        # 在Meta中, 重新定义, 改动字段属性
        extra_kwargs = {
            'password': {
                'write_only': True,
                'min_length': 8,
                'max_length': 32,
            },

        }

    def validate_mobile(self, value):
        if value is None:
            return ''
        if not re.match(r'^1[3-9]\d{9}$', value):
            raise serializers.ValidationError('请输入正确的手机号码')
        return value

    def validate_allow(self, value):
        if value != 'true':
            raise serializers.ValidationError('请点击同意协议')
        return value

    def validate_username(self, value):
        if User.objects.filter(username=value):
            raise serializers.ValidationError('当前用户名已存在')

        return value

    def validate(self, attrs):
        password = attrs['password']
        password2 = attrs['password2']
        if password != password2:
            raise serializers.ValidationError('密码不匹配')
        return attrs

    def create(self, validated_data):

        # 删除用户提交的多余数据创建用户
        del validated_data['password2']
        del validated_data['allow']
        user = super(CreateUserSerializer).create(validated_data)
        user.set_password(validated_data['password'])
        user.save()

        # 生成jwt token
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER

        payload = jwt_payload_handler(user)
        token = jwt_encode_handler(payload)

        user.token = token
        return user
