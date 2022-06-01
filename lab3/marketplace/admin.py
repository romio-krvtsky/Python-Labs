from django.contrib import admin
from .models import *


# Register your models here.
class UserAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'email', 'phone',)
    list_display_links = ('username',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'state', 'post_date', 'owner',)
    list_display_links = ('name',)


admin.site.register(User, UserAdmin)
admin.site.register(Product, ProductAdmin)
