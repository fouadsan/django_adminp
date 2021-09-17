from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from blog.admin import blog_site


urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
