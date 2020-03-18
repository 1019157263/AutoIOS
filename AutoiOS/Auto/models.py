from django.db import models
import django.utils.timezone as timezone
import os
from django.utils.html import format_html
# Create your models here.

class AutoiOS(models.Model):
    COM = models.CharField(max_length=200)
    add_date = models.DateTimeField('保存日期',default = timezone.now)
    
    photo = models.ImageField(upload_to="icons")
    Conphoto = models.ImageField(upload_to="icons")
    ConLen = models.IntegerField(default=0,)

    def image_data(self):
        return format_html('<a href={} ><img src="{}" width="150px"/></a>',self.photo.url,self.photo.url)

    image_data.short_description = u'原始图片'
    def len_x(self):
        return self.ConLen

    len_x.short_description=u"计算拖动长度"

    def image_resdata(self):
        return format_html(
            '<a href={} ><img src="{}" width="150px"/></a>',self.Conphoto.url,self.Conphoto.url)

    image_resdata.short_description = u'处理图'


    def __str__(self):
        return self.COM

