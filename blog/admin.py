from django.contrib import admin
from .models import Post


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Admin Area'


blog_site = BlogAdminArea(name='BlogAdmin')

blog_site.register(Post)
