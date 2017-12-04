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
    comment = models.CharField(max_length= 255, default = "요청사항을 기재해주세요")
    file = models.FileField(upload_to = user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    pub_date = models.DateTimeField(auto_now_add=True)
    volume = models.IntegerField(default = 0)
    price = models.CharField(max_length = 255 ,  default ="검토중")
    time = models.CharField(max_length = 255 , default ="검토중")
    address = models.CharField(max_length=255)
    phone_number = models.CharField(max_length = 255)
    thumnail_image = models.ImageField(blank = True)
    filenamemake = models.CharField(max_length=255)
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
        return "%s %s %s %s %s" % (self.owner , self.file ,self.pub_date , self.address , self.phone_number )

# class CustomAddress(models.Model):
#     owner = models.ForeignKey(settings.AUTH_USER_MODEL)
#     address = models.CharField(max_length = 255 , default = u"여기에 주소를 입력해주세요, 구/신주소 무관")
#     phone_number = models.IntegerField(default = u"-는 생략해주세요")
#     def generate(self):
#         self.save()
#         return self.owner
#     def __str__(self):
#         return "%s %s %s " % (self.owner , self.address ,self.phone_number )
