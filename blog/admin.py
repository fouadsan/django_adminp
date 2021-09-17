from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog  Admin Area'
    login_template = 'blog/admin/login.html'


blog_site = BlogAdminArea(name='BlogAdmin')


class SummerAdmin(SummernoteModelAdmin):
    summernote_fields = '__all__'


admin.site.register(Post, SummerAdmin)
blog_site.register(Post, SummerAdmin)
