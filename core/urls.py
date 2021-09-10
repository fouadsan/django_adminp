from django.contrib import admin
from django.urls import path

from blog.admin import blog_site
from bookstore.admin import bookstore_site

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blogadmin/', blog_site.urls),
    path('bookstoreadmin/', bookstore_site.urls),
]


# admin.site.index_title = "The Bookstore"
# admin.site.site_header = "The Bookstore Admin"
# admin.site.site_title = "Site Title Bookstore"
