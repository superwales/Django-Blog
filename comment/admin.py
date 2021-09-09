from comment.models import Comment
from django.contrib import admin
from django.db import models

from myblog.custom_site import custom_site
from .models import Comment

# Register your models here.
@admin.register(Comment, site=custom_site)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('target', 'targetname', 'nickname', 'content', 'email', 'created_time')