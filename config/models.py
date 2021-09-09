from django.db import models
from django.contrib.auth.models import User
from django.template.loader import render_to_string


# Create your models here.
class SideBar(models.Model):
    STATUS_SHOW = 1
    STATUS_HIDE = 0
    STATUS_ITEMS = (
        (STATUS_SHOW, "展示"),
        (STATUS_HIDE, "隐藏"),
    )
    HTML = 1
    LATEST = 2
    HOT = 3
    COMMENT = 4
    SIDE_TYPE = (
        (HTML, 'HTML'), 
        (LATEST, "最新文章"),
        (HOT, "最热文章"),
        (COMMENT, "最近评论"),
    )
    title = models.CharField(max_length=50, verbose_name="标题")
    display_type = models.PositiveIntegerField(default=1, choices=SIDE_TYPE, verbose_name="展示类型")
    content = models.CharField(max_length=500, blank=True, verbose_name="内容", help_text="如果设置的不是HTML类型，可为空")
    status = models.PositiveIntegerField(default=STATUS_SHOW, choices=STATUS_ITEMS, verbose_name="状态")
    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="作者")
    created_time = models.DateTimeField(auto_now_add=True, verbose_name="创建时间")

    class Meta:
        verbose_name = verbose_name_plural = "侧边栏"
    
    def __str__(self):
        return self.title
    
    @classmethod
    def get_all(cls):
        return cls.objects.filter(status=cls.STATUS_SHOW)
    
    @property
    def content_html(self):
        from blog.models import Post
        from comment.models import Comment

        result = ""
        if self.display_type == self.HTML:
            result = self.content
        elif self.display_type == self.LATEST:
            context = {
                'posts': Post.latest_posts()
            }
            result = render_to_string('config/block/sidebar_posts.html', context)
        elif self.display_type == self.HOT:
            context = {
                'post': Post.hot_posts()
            }
            result = render_to_string('config/block/sidebar_posts.html', context)
        elif self.display_type == self.COMMENT:
            context = {
                'comments': Comment.objects.filter(status=Comment.STATUS_NORMAL)
            }
            result = render_to_string('config/block/sidebar_comments.html', context)
        return result