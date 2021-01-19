# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from django.http import HttpResponse,JsonResponse
import json
from django.conf import settings
from rest_framework.response import Response
from rest_framework.views import APIView
from utils.security import decrypt
# Create your views here.
import hashlib
import time
from api import models
from utils.service import process_basic,process_disk,process_memory,process_nic

def gen_sign(ctime):
    val = '%s|%s' %(settings.URL_AUTH_KEY,ctime)
    obj = hashlib.md5()
    obj.update(val.encode('utf-8'))
    return obj.hexdigest()

SIGN_RECORD = {}

class APIAuthView(APIView):
    def dispatch(self, request, *args, **kwargs):
        client_sign=request.GET.get('sign')
        client_ctime=int(request.GET.get('ctime'))
        server_time=int(time.time() * 1000)
        if server_time - client_ctime > 3000:
            return JsonResponse({'status':False,'error':"it takes too long time"})
        if client_sign in SIGN_RECORD:
            return JsonResponse({'status': False, 'error': "it has used"})
        server_sign = gen_sign(client_ctime)
        if server_sign != client_sign:
            return JsonResponse({'status': False, 'error':"it has wrong sign"})
        SIGN_RECORD[client_sign]=client_ctime
        print("the sign is ok!")
        return super(APIAuthView, self).dispatch(request, *args, **kwargs)

class server(APIAuthView):
    def get(self,request,*args,**kwargs):
        hostlist = ['c1.com', 'c2.com', 'c3.com']
        return Response(hostlist)

    def post(self,request,*args,**kwargs):
        body = decrypt(request._request.body)
        asset_info = json.loads(body.decode('utf-8'))
        result = {'status': True, 'data': "tf67", 'error': None}
        asset_type = asset_info.get('type')
        if asset_type == 'create':
            server_dict = {}
            server_dict.update(asset_info['basic']['data'])
            server_dict.update(asset_info['cpu']['data'])
            server_dict.update(asset_info['board']['data'])
            server=models.Server.objects.create(**server_dict)
            disk_info = asset_info['disk']['data']
            for k, v in disk_info.items():
                v['server'] = server
                print("test", v)
                models.Disk.objects.create(**v)
            net_info = asset_info['net']['data']
            for k, v in net_info.items():
                v['server'] = server
                v['name'] = k
                models.NIC.objects.create(**v)
            mem_info = asset_info['mem']['data']
            for k, v in mem_info.items():
                v['server'] = server
                models.Memory.objects.create(**v)
        elif asset_type == 'update':
            hostname = asset_info['basic']['data']['hostname']
            server = models.Server.objects.filter(hostname=hostname).first()
            process_basic(asset_info,hostname)
            process_memory(asset_info,server)
            process_disk(asset_info,server)
            process_nic(asset_info,server)
        elif asset_type == 'host_update':
            hostname = str(asset_info['cert'])
            print("zhou2",hostname)
            server = models.Server.objects.filter(hostname=hostname).first()
            print("zhou22",server)
            process_basic(asset_info, hostname)
            process_memory(asset_info, server)
            process_disk(asset_info, server)
            process_nic(asset_info, server)
        result['data']=asset_info['basic']['data']['hostname']
        return Response(result)
