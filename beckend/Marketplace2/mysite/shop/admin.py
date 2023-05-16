from django.contrib import admin
from .models import *



class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created']
    list_filter = ['available', 'created']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}
admin.site.register(Product, ProductAdmin)



# class SchoolAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'password']
#     # prepopulated_fields = {'slug': ('name',)}
admin.site.register(School)



# class UserAdmin(admin.ModelAdmin):
#     list_display = ['products_name', 'info']
#     # prepopulated_fields = {'slug': ('name',)}
admin.site.register(User)
