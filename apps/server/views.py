from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.json_rpc import SoftetherAPI


# logging.captureWarnings(True)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Info(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        softapi = SoftetherAPI()
        resp = softapi.GetServerInfo()
        if 'error' in resp:
            res['code'] = 1
            res['data'] = resp
        else:
            res['data'] = resp
    return Response(res)


@api_view(['GET'])
def Status(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        softapi = SoftetherAPI()
        resp = softapi.GetServerStatus()
        if 'error' in resp:
            res['code'] = 1
            res['data'] = resp
        else:
            res['data'] = resp
    return Response(res)


@api_view(['POST'])
def Setpwd(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'POST':
        password = request.data.get('password')
        if password:
            softapi = SoftetherAPI()
            resp = softapi.SetServerPassword(PlainTextPassword_str=password)
            if 'error' in resp:
                res['code'] = 1
                res['data'] = resp
            else:
                res['data'] = resp
        else:
            res['code'] = 1
            res['msg'] = '参数不足'
    return Response(res)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def Ssl(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        softapi = SoftetherAPI()
        resp = softapi.GetServerCert()
        if 'error' in resp:
            res['code'] = 1
            res['data'] = resp
        else:
            res['data'] = resp


    elif request.method == 'POST':
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass

    return Response(res)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def Cipher(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        softapi = SoftetherAPI()
        resp = softapi.GetServerCipher()
        if 'error' in resp:
            res['code'] = 1
            res['data'] = resp
        else:
            res['data'] = resp

    elif request.method == 'POST':
        str = request.data.get('str')
        if str:
            softapi = SoftetherAPI()
            resp = softapi.SetServerCipher(String_str=str)
            if 'error' in resp:
                res['code'] = 1
                res['data'] = resp
            else:
                res['data'] = resp
        else:
            res['code'] = 1
            res['msg'] = '参数不足'


    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass

    return Response(res)


@api_view(['GET', 'POST', 'DELETE', 'PUT'])
def Hub(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        # 获取Hub列表 和 Hub配置
        hubname = request.query_params.get('hubname')
        softapi = SoftetherAPI()
        if hubname:
            resp = softapi.GetHub(HubName_str=hubname)
        else:
            resp = softapi.EnumHub()
        if 'error' in resp:
            res['code'] = 1
            res['data'] = resp
        else:
            res['data'] = resp

    elif request.method == 'POST':
        # 创建Hub
        hubname = request.data.get('hubname')
        password = request.data.get('password')
        status = request.data.get('status')
        type = request.data.get('type')
        max = request.data.get('max')
        enum = request.data.get('enum')
        if all([hubname, password, status, type, max, ]):
            softapi = SoftetherAPI()
            resp = softapi.CreateHub(HubName_str=hubname,
                                     AdminPasswordPlainText_str=password,
                                     Online_bool=status if status in [True, False] else True,
                                     NoEnum_bool=enum,
                                     MaxSession_u32=max,
                                     HubType_u32=type,
                                     )
            if 'error' in resp:
                res['code'] = 1
                res['data'] = resp
            else:
                res['data'] = resp
        else:
            res['code'] = 1
            res['msg'] = '参数不足'

    elif request.method == 'PUT':
        # 更改Hub配置
        data = request.data.copy()
        hubname = data.get('hubname')
        if hubname:
            softapi = SoftetherAPI()
            resp = softapi.SetHub(**data)
            if 'error' in resp:
                res['code'] = 1
                res['data'] = resp
            else:
                res['data'] = resp
        else:
            res['code'] = 1
            res['msg'] = '参数不足'

    elif request.method == 'DELETE':
        # 删除Hub
        hubname = request.data.get('hubname')
        if hubname:
            softapi = SoftetherAPI()
            resp = softapi.DeleteHub(HubName_str=hubname)
            if 'error' in resp:
                res['code'] = 1
                res['data'] = resp
            else:
                res['data'] = resp
        else:
            res['code'] = 1
            res['msg'] = '参数不足'

    return Response(res)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Tcp(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        # 获取连接到VPN服务器的TCP连接列表/ 获取连接到VPN服务器的TCP连接的信息
        name = request.query_params.get('name')
        softapi = SoftetherAPI()
        if name:
            resp = softapi.GetConnectionInfo(Name_str=name)
        else:
            resp = softapi.EnumConnection()
        if 'error' in resp:
            res['code'] = 1
            res['data'] = resp
        else:
            res['data'] = resp

    elif request.method == 'POST':
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        # 断开连接到VPN服务器的TCP连接
        name = request.data.get('name')
        if name:
            softapi = SoftetherAPI()
            resp = softapi.DisconnectConnection(Name_str=name)
            if 'error' in resp:
                res['code'] = 1
                res['data'] = resp

            else:
                res['data'] = resp

        else:
            res['code'] = 1
            res['msg'] = '参数不足'

    return Response(res)


@api_view(['POST'])
def Ca(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        hubname = request.query_params.get('hubname')
        key = request.query_params.get('key')
        softapi = SoftetherAPI()
        if hubname and key:
            # 获取可信CA证书
            resp = softapi.GetCa(HubName_str=hubname,
                                 Key_u32=key)
            if 'error' in resp:
                res['code'] = 1
                res['data'] = resp

            else:
                res['data'] = resp

        elif hubname:
            # 获取可信CA证书列表
            resp = softapi.EnumCa(HubName_str=hubname)
            if 'error' in resp:
                res['code'] = 1
                res['data'] = resp

            else:
                res['data'] = resp

        else:
            res['code'] = 1
            res['msg'] = '参数不足'

    elif request.method == 'POST':
        # 添加可信CA证书
        hubname = request.data.get('hubname')
        certbin = request.data.get('certbin')
        if hubname and certbin:
            softapi = SoftetherAPI()
            resp = softapi.AddCa(Cert_bin=certbin,
                                 HubName_str=hubname)
            if 'error' in resp:
                res['code'] = 1
                res['data'] = resp

            else:
                res['data'] = resp
        else:
            res['code'] = 1
            res['msg'] = '参数不足'

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        # 删除可信CA证书
        hubname = request.data.get('hubname')
        key = request.data.get('key')
        if hubname and key:
            softapi = SoftetherAPI()
            resp = softapi.DeleteCa(Key_u32=key,
                                    HubName_str=hubname)
            if 'error' in resp:
                res['code'] = 1
                res['data'] = resp

            else:
                res['data'] = resp

        else:
            res['code'] = 1
            res['msg'] = '参数不足'
    return Response(res)


@api_view(['POST'])
def Hubconfig(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'POST':
        action = request.data.get('action')
        if action:
            softapi = SoftetherAPI()
            if action == 'GetHubLog':
                # 获取虚拟HUB的日志记录配置
                hubname = request.data.get('hubname')
                if hubname:
                    resp = softapi.GetHubLog(HubName_str=hubname)
                    if 'error' in resp:
                        res['code'] = 1
                        res['data'] = resp

                    else:
                        res['data'] = resp
                else:
                    res['code'] = 1
                    res['msg'] = '参数不足'

            elif action == 'SetHubLog':
                # 设置虚拟HUB的日志记录配置
                data = request.data.copy()
                hubname = data.get('hubname')
                if hubname:
                    resp = softapi.GetHubLog(**data)
                    if 'error' in resp:
                        res['code'] = 1
                        res['data'] = resp

                    else:
                        res['data'] = resp
                else:
                    res['code'] = 1
                    res['msg'] = '参数不足'

            elif action == 'SetHubLog':
                # 获取虚拟HUB的当前状态
                hubname = request.data.get('hubname')
                if hubname:
                    resp = softapi.GetHubStatus(HubName_str=hubname)
                    if 'error' in resp:
                        res['code'] = 1
                        res['data'] = resp

                    else:
                        res['data'] = resp
                else:
                    res['code'] = 1
                    res['msg'] = '参数不足'

            elif action == 'SetHubOnline':
                # 将虚拟HUB切换到联机或脱机
                hubname = request.data.get('hubname')
                status = request.data.get('status', True)
                if hubname:
                    resp = softapi.GetHubStatus(HubName_str=hubname,
                                                Online_bool=status)
                    if 'error' in resp:
                        res['code'] = 1
                        res['data'] = resp

                    else:
                        res['data'] = resp
                else:
                    res['code'] = 1
                    res['msg'] = '参数不足'
            else:
                res['code'] = 1
                res['msg'] = '无当前操作'


        else:
            res['code'] = 1
            res['msg'] = '参数不足'

    return Response(res)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Access(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass
    return Response(res)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Link(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        pass

    elif request.method == 'POST':
        pass

    elif request.method == 'PUT':
        pass

    elif request.method == 'DELETE':
        pass

    return Response(res)