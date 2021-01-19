



# -*- coding: utf-8 -*-

from django.db import models

# Create your models here.

class BusinessUnit(models.Model):
    name=models.CharField("yewuxian",max_length=64,unique=True)
    class Meta:
        verbose_name_plural="yewuxianbiao"
    def __str__(self):
        return self.name

class IDC(models.Model):
    name=models.CharField("jifang",max_length=32)
    floor=models.CharField("loucheng",max_length=16,default=1)
    class Meta:
        verbose_name_plural="IDCbiao"
    def __str__(self):
        return self.name

class Server(models.Model):
    device_status_choices=(
        (1,'shangjia'),
        (2, 'online'),
        (3, 'offline'),
        (4, 'xiajia'),
    )
    device_status_id = models.IntegerField(verbose_name="zhuangtai",choices=device_status_choices,default=1)
    idc = models.ForeignKey('IDC',verbose_name="IDCjifang",null=True,blank=True)
    cabinet_num=models.CharField('jiguihao',max_length=32,null=True,blank=True)
    cabinet_order=models.CharField('jiguizhongxuhao',max_length=32,null=True,blank=True)

    business_unit=models.ForeignKey('BusinessUnit',verbose_name="shuyudeyewuxian",null=True,blank=True)

    hostname=models.CharField(verbose_name="zhujiming",max_length=128,unique=True)
    os_platform=models.CharField("system",max_length=32,null=True,blank=True)
    os_version=models.CharField('systemversion',max_length=32,null=True,blank=True)

    sn=models.CharField('snnum',max_length=32,db_index=True)
    manufacturer=models.CharField(verbose_name="zhizhaoshang",max_length=32,null=True,blank=True)
    model=models.CharField("xinghao",max_length=32,null=True,blank=True)

    cpu_count=models.IntegerField('CPUgeshu',null=True,blank=True)
    cpu_physical_count=models.IntegerField('CPUwuligeshu',null=True,blank=True)
    cpu_model=models.CharField('CPUxinghao',max_length=128,null=True,blank=True)

    latest_date= models.DateField(null=True)
    create_at=models.DateTimeField(auto_now_add=True,blank=True)

    class Meta:
        verbose_name_plural="fuwuqibiao"
    def __str__(self):
        return self.hostname

class Disk(models.Model):
    slot = models.CharField('chachaowei',max_length=16)
    model = models.CharField('yinpanxinghao',max_length=32)
    capacity = models.FloatField('cipanrongliangGB')
    pd_type=models.CharField('cipanleixing',max_length=32)
    server = models.ForeignKey(verbose_name='fuwuqi',to='Server',related_name='disk_list')

    class Meta:
        verbose_name_plural="Diskbiao"
    def __str__(self):
        return self.slot

class NIC(models.Model):
    name=models.CharField('wangkamingcheng',max_length=64)
    hwaddr=models.CharField('wangkamacdizhi',max_length=64)
    netmask=models.CharField(max_length=32)
    ipaddrs=models.CharField('ipdizhi',max_length=64)
    up=models.BooleanField(default=False)
    server=models.ForeignKey('Server',related_name='nic_list')

    class Meta:
        verbose_name_plural="NICbiao"
    def __str__(self):
        return self.name

class Memory(models.Model):
    slot=models.CharField('chachaowei',max_length=32)
    manufacturer=models.CharField('zhizhaoshang',max_length=32,null=True,blank=True)
    model=models.CharField('xinghao',max_length=32)
    capacity=models.FloatField('rongliang',null=True,blank=True)
    sn=models.CharField('neicunsn',max_length=16,null=True,blank=True)
    speed=models.CharField('speed',max_length=16,null=True,blank=True)

    server=models.ForeignKey('Server',related_name='memory_list')
    class Meta:
        verbose_name_plural="Memorybiao"
    def __str__(self):
        return self.slot

class AssetRecord(models.Model):
    server = models.ForeignKey('Server',related_name='servers')
    content=models.TextField(null=True)
    create_at=models.DateTimeField(auto_now_add=True)
    class Meta:
        verbose_name_plural="zichanjilubiao"

class ErrorLog(models.Model):
    server=models.ForeignKey('Server',null=True,blank=True)
    title=models.CharField(max_length=32)
    content=models.TextField()
    create_at=models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural="cuowurizhibiao"
    def __str__(self):
        return self.title
