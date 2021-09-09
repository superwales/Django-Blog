from django.db import models
from django.forms.widgets import Textarea
from django.utils import tree

from blog.models import Post


# Create your models here.
class Comment(models.Model):
    STATUS_NORMAL = 1
    STATUS_DELETE = 0
    STATUS_ITEMS = (
        (STATUS_NORMAL, "正常"),
        (STATUS_DELETE, "删除"),
    )

    target = models.CharField(max_length=100, verbose_name="评论目标")
    targetname = models.CharField(max_length=255, default="", verbose_name="评论目标名称")
    content = models.CharField(max_length=2000, verbose_name="内容")
    nickname = models.CharField(max_length=50, verbose_name="昵称")
    email = models.EmailField(verbose_name="邮箱", blank=True)
    status = models.PositiveIntegerField(default=STATUS_NORMAL, choices=STATUS_ITEMS, verbose_name="状态")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "评论"
    
    def __str__(self):
        return self.content[:20]
    
    @classmethod
    def get_by_target(cls, target):
        return cls.objects.filter(target=target, status=cls.STATUS_NORMAL)
