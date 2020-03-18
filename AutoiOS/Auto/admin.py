from django.contrib import admin

# Register your models here.
from django.contrib import admin

from .models import AutoiOS


# class AutoiOSAdmin(admin.ModelAdmin):
#     fields = ['COM', 'add_date','ConLen'.'photo']#只显示这些
#@admin.register(AutoiOS)
class AutoiOSAdmin(admin.ModelAdmin):
    fields = ['COM', 'add_date','ConLen','image_data',"image_resdata"]#只显示这些
    list_display = ('COM', 'image_data',"image_resdata","len_x","add_date")
    readonly_fields = ('image_data',"image_resdata")

admin.site.register(AutoiOS,AutoiOSAdmin)