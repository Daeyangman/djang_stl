from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import numpy as np
from stl import mesh
from django.db import models
import datetime
from django.utils import timezone
# Create your models here.
def user_path(instance , filename):
    # from random import choice
    # import string
    # arr =  [choice(string.ascii_letters) for _ in range(8) ]
    # pid = ''.join(arr)
    # extension = filename.split('.')[1]
    # return '%s/%s.%s' % (instance.owner.username , pid , extension)
    return '%s/%s' % (instance.owner.username,filename)



class StlFile(models.Model):
    comment = models.CharField(max_length= 255, blank=True)
    file = models.FileField(upload_to = user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    pub_date = models.DateTimeField(auto_now_add=True)
    volume = models.IntegerField(default = 0)
    price = models.CharField(max_length = 255 ,  default ="검토중")
    time = models.CharField(max_length = 255 , default ="검토중")

    thumnail_image = models.ImageField(blank = True)
    filenamemake = models.CharField(max_length=255)
    fdm_material_price = models.IntegerField(blank = True,default = 0)
    fdm_time = models.IntegerField(blank = True,default = 0)
    fdm_machine_price = models.IntegerField(blank=True,default = 0)
    fdm_sum_price = models.IntegerField(blank=True,default = 0)
    sla_material_price = models.IntegerField(blank=True,default = 0)
    sla_time = models.IntegerField(blank = True,default = 0)
    sla_machine_price = models.IntegerField(blank=True,default = 0)
    sla_sum_price = models.IntegerField(blank=True,default = 0)
    sla_sum_time = models.IntegerField(blank = True , default = 0)
    fdm_sum_time = models.IntegerField(blank = True , default = 0)
    test_a = models.CharField(blank=True , max_length=255)
    test_b = models.CharField(blank=True, max_length = 255)
    def sum_price(self):
        self.save()
        self.fdm_sum_price = self.fdm_machine_price + self.fdm_material_price
        self.sla_sum_price = self.sla_machine_price + self.sla_material_price
        return self.fdm_sum_price , self.sla_sum_price
    def filenameMake(self):
        self.save()
        self.filenamemake = self.file.name.split('/')[1]
        return self.filenamemake

    def meshMake(self):
        self.save()
        self.mesh = mesh.Mesh.from_file(self.file.path)
        self.volume ,b,c = self.mesh.get_mass_properties()
        return self.volume
    def __str__(self):
        return "%s %s %s" % (self.owner , self.file ,self.pub_date)


class CustomAddress(models.Model):
    stlfile = models.ForeignKey(StlFile)
    author = models.ForeignKey(settings.AUTH_USER_MODEL)
    address = models.CharField(max_length=255, blank=True)
    detail_address = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255, blank=True)
    name_user = models.CharField(max_length=255 , blank =True)
    def __str__(self):
        return "%s %s %s" % (self.author, self.address, self.phone_number)
