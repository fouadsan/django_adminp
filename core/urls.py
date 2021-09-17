from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]


admin.site.index_title = "The Bookstore"
admin.site.site_header = "The Bookstore Admin"
admin.site.site_title = "Site Title Bookstore"
