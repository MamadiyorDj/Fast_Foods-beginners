from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Categories)
admin.site.register(Products)
admin.site.register(Users)
admin.site.register(Fastfoods)
admin.site.register(Orders)
admin.site.register(Order_items)