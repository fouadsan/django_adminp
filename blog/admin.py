from django.contrib import admin
import django.apps

# from .models import Category, Post

models = django.apps.apps.get_models()
# print(models)

for model in models:
    try:
        admin.site.register(model)
    except admin.sites.AlreadyRegistered:
        pass

admin.site.unregister(django.contrib.sessions.models.Session)

# admin.site.register(Category)
# admin.site.register(Post)


# @admin.register(Post)
# class PostAdmin(admin.ModelAdmin):
#     fields = ['title', 'author']


# admin.site.register(Post, PostAdmin)
