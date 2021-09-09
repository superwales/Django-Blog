from django.contrib import admin

from myblog.custom_site import custom_site
from .models import SideBar


# Register your models here.
@admin.register(SideBar, site=custom_site)
class SidebarAdmin(admin.ModelAdmin):
    list_display = ('title', 'display_type', 'content', 'created_time')
    fields = ('title', 'display_type', 'content')

    def save_model(self, request, obj, form, change):
        obj.owner = request.user
        return super(SidebarAdmin, self).save_model(request, obj, form, change)