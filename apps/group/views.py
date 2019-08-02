import logging

from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view
from rest_framework.response import Response
from utils.json_rpc import SoftetherAPI
# logging.captureWarnings(True)

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def tmp(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        hubname = request.query_params.get('hubname')

        return Response(res)

    elif request.method == 'POST':

        return Response(res)

    elif request.method == 'PUT':

        return Response(res)

    elif request.method == 'DELETE':

        return Response(res)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Grouplist(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        hubname = request.query_params.get('hubname')
        if hubname:
            softapi = SoftetherAPI()
            resp = softapi.EnumGroup(HubName_str=hubname)
            if 'error' in resp:
                res['code'] = 1
                resp['data'] = resp
            else:
                res['data'] = resp['GroupList'] if 'GroupList' in resp else []

        else:
            res['code'] = 1
            res['msg'] = '缺少参数'

        return Response(res)

    elif request.method == 'POST':
        data = request.data.copy()
        hubname = data.pop('hubname') if 'hubname' in data else None
        name = data.pop('name') if 'name' in data else None
        # realname = request.data.get('realname')
        # description = request.data.get('description')

        if name and hubname:
            softapi = SoftetherAPI()
            resp = softapi.CreateGroup(HubName_str=hubname, Name_str=name, **data)
            if 'error' in resp:
                res['code'] = 1
                resp['data'] = resp
            else:
                res['data'] = resp
        else:
            res['code'] = 1
            res['msg'] = '参数不足'
        return Response(res)

    elif request.method == 'PUT':

        return Response(res)

    elif request.method == 'DELETE':
        username = request.data.get('username')
        groupname = request.data.get('groupname')
        hubname = request.data.get('hubname')
        name = username or groupname
        if hubname and name:
            softapi = SoftetherAPI()
            resp = softapi.DeleteGroup(HubName_str=hubname, Name_str=name)
            if 'error' in resp:
                res['code'] = 1
                res['data'] = resp

            else:
                res['data'] = resp
        else:
            res['code'] = 1
            res['msg'] = '缺少参数'
        return Response(res)


@api_view(['GET'])
def Vpnsession(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        hubname = request.query_params.get('hubname')
        if hubname:
            softapi = SoftetherAPI()
            resp = softapi.EnumSession(HubName_str=hubname)
            if 'error' in resp:
                res['code'] = 1
                resp['data'] = resp
            else:
                res['data'] = resp['SessionList'] if 'SessionList' in resp else []

        else:
            res['code'] = 1
            res['msg'] = '缺少参数'

        return Response(res)

    elif request.method == 'POST':

        return Response(res)

    elif request.method == 'PUT':

        return Response(res)

    elif request.method == 'DELETE':

        return Response(res)


@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def Groupconfig(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'GET':
        hubname = request.query_params.get('hubname')
        groupname = request.query_params.get('groupname')
        if hubname and groupname:
            softapi = SoftetherAPI()
            resp = softapi.GetGroup(HubName_str=hubname, Name_str=groupname)
            if 'error' in resp:
                res['code'] = 1
                resp['data'] = resp
            else:
                res['data'] = resp

        else:
            softapi = SoftetherAPI()
            resp = softapi.EnumSession()
            res['data'] = resp['SessionList'] if 'SessionList' in resp else []
        return Response(res)

    elif request.method == 'POST':

        return Response(res)

    elif request.method == 'PUT':

        return Response(res)

    elif request.method == 'DELETE':

        return Response(res)


@api_view(['POST'])
def Removeuser(request):
    res = {'code': 0, 'msg': '', 'data': ''}
    if request.method == 'POST':
        pass
