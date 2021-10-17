from django.contrib import admin
from . models import *


# Register your models here.
class categadmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
admin.site.register(categ,categadmin)

class prodAdmin(admin.ModelAdmin):
    list_display = ['name','slug','img','price','stock','available']
    list_editable=['price','stock','available','img']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(products,prodAdmin)


