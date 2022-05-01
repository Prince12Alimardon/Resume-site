from django.contrib import admin
from .models import Service, Category, GetInTouch


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('id', 'profession')


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'category')


class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email')


admin.site.register(Service, ServiceAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(GetInTouch, GetInTouchAdmin)
