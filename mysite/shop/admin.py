# -*- coding: utf8 -*-
from django.contrib import admin
from .models import *


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}


admin.site.register(Category, CategoryAdmin)


class UserAdmin(admin.ModelAdmin):
    save_on_top = True
    list_display = [
        "id",
        "name",
    ]
    readonly_fields = ["id", ]
    list_display_links = (
        "id",
        "name",
    )
    ordering = ("id",)


admin.site.register(User, UserAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'price', 'stock', 'available', 'created']
    list_filter = ['available', 'created']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'slug': ('name',)}


class BasketAdmin(admin.ModelAdmin):
    list_display = ['product', 'user', 'created_at', 'updated_at', ]


admin.site.register(Basket, BasketAdmin)

admin.site.register(Product, ProductAdmin)

# class SchoolAdmin(admin.ModelAdmin):
#     list_display = ['name', 'email', 'password']
#     # prepopulated_fields = {'slug': ('name',)}
admin.site.register(School)
