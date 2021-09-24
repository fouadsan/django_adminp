from django.contrib import admin
from django.contrib import messages

from .models import Post, Book


class BlogAdminArea(admin.AdminSite):
    site_header = 'Blog Database'


class TestAdminPermissions(admin.ModelAdmin):
    def has_add_permission(self, request):
        return False

    def has_change_permission(self, request, obj=None):
        return False

    def has_delete_permission(self, request, obj=None):
        if obj != None and request.POST.get('action') == 'delete_selected':
            messages.add_message(request, messages.ERROR, (
                "I really hope you are sure about this!"
            ))

        return True

        # if request.user.groups.filter(name='editors').exists():
        #     return True

        # return True
        # return obj is None or obj.pk != 1
        # return obj is None or obj.title != 'post1'

    def has_view_permission(self, request, obj=None):
        return True


blog_site = BlogAdminArea(name='BlogAdmin')

blog_site.register(Post, TestAdminPermissions)
blog_site.register(Book)
