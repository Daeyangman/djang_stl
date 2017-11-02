from django.db import models
from django.contrib.auth.models import User
from django.conf import settings
import numpy as np
from stl import mesh
# Create your models here.
def user_path(instance , filename):
    from random import choice
    import string
    arr =  [choice(string.ascii_letters) for _ in range(8) ]
    pid = ''.join(arr)
    extension = filename.split('.')[-1]
    return '%s/%s.%s' % (instance.owner.username , pid , extension)

class StlFile(models.Model):
    stl = models.FileField(upload_to = user_path)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL)
    pub_date = models.DateTimeField(auto_now_add=True)
    volume = models.IntegerField(default = 0)
    def meshMake(self):
        self.save()
        self.mesh = mesh.Mesh.from_file(self.stl.path)
        self.volume ,b,c = self.mesh.get_mass_properties()
        return self.volume
    def __str__(self):
        return "%s %s %s " % (self.owner , self.stl ,self.pub_date )