from django.contrib import admin
from app_silkshadow.models import item

# Register your models here.
class admin_item(admin.ModelAdmin):
    list_display=['product','desc','price']

admin.site.register(item,admin_item)



