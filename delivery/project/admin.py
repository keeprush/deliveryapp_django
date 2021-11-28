from django.contrib import admin
from .models import Order_info, Users,Storekeepers,Reviews

# Register your models here.

admin.site.register(Users)
admin.site.register(Storekeepers)
admin.site.register(Reviews)
admin.site.register(Order_info)