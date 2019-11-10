from django.db import models
from django.contrib.auth.models import User
import uuid

# Create your models here.
class Plant(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    parent = models.ForeignKey(User, on_delete=models.CASCADE)
    alias  = models.CharField(max_length=20, default=None, null=True, blank=True)
    lat = models.FloatField(default = 13.5115)
    lon = models.FloatField(default = 80.0144)

    def __str__(self):
        if self.alias:
            return self.alias
        return str(self.id)

    def get_absolute_url(self):
        return "/plant" +  "/"+ str(self.alias)



class Waterdata(models.Model):
    #id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    district  = models.CharField(max_length=20, default=None, null=True, blank=True)
    zone  = models.CharField(max_length=200, default=None, null=True, blank=True)
    settlement  = models.CharField(max_length=200, default=None, null=True, blank=True)
    block  = models.CharField(max_length=20, default=None, null=True, blank=True)
    cluster  = models.CharField(max_length=20, default=None, null=True, blank=True)
    source  = models.CharField(max_length=200, default=None, null=True, blank=True)
    dwdnum = models.CharField(max_length=200, default=None, null=True, blank=True)
    ycord  = models.CharField(max_length=200, default=None, null=True, blank=True)
    xcord  = models.CharField(max_length=200, default=None, null=True, blank=True)
    parameter  = models.CharField(max_length=200, default=None, null=True, blank=True)
    freeresid = models.CharField(max_length=100, default=None, null=True, blank=True)
    turbidity  = models.CharField(max_length=80, default=None, null=True, blank=True)
    ecol  = models.CharField(max_length=20, default=None, null=True, blank=True)
    ph  = models.CharField(max_length=20, default=None, null=True, blank=True)


    def get_absolute_url(self):
        return "/plant" +  "/"+ str(self.id)