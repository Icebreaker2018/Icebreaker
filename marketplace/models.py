from django.db import models
from django.db.models import PROTECT
from django.contrib.auth.models import User
from PIL import Image
from django.utils import timezone
import datetime
from datetime import timedelta

class product(models.Model):
    fullname = models.ForeignKey(User, on_delete=models.PROTECT,null = True, blank = True) #foreign key from user table from django-admin
    product_title = models.CharField(max_length = 100,)
    product_type = models.CharField(null=True, max_length = 100)
    overview = models.TextField()
    date = models.DateTimeField(auto_now_add = True)
    image = models.ImageField(upload_to="media", blank=True)
    cost = models.FloatField(null = True)
    quantity = models.IntegerField(null = True)
#    pic = models.ForeignKey(profile, on_delete=models.PROTECT,null = True, blank = True)

    def __str__(self):
        return self.product_title

    def snippept(self):
        return self.overview[:50] + "..."

class Transcation(models.Model):
    name = models.CharField(max_length=30)
    product_title = models.ForeignKey(product, on_delete=models.PROTECT,null = True, blank = True)
    product_type = models.CharField(null=True, max_length = 100)
    cost = models.FloatField(null = True)
    token = models.CharField(max_length = 20)
    date_backed = models.DateTimeField(default=timezone.now)
