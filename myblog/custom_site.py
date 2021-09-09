from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = "个人博客"
    site_title = "个人博客管理后台"
    index_title = "首页"

custom_site = CustomSite(name = 'cus_admin')