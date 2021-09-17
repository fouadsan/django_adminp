from django.contrib import admin
from django import forms

from .models import Post


class PostForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(args, **kwargs)
        self.fields['title'].help_text = "New Help Text"

    class Meta:
        model = Post
        exclude = ('slug',)


class PostFormAdmin(admin.ModelAdmin):
    form = PostForm


admin.site.register(Post, PostFormAdmin)

# TEXT = 'Some text that we can include'


# class PostAdmin(admin.ModelAdmin):

# grouped fields
#     fields = ['title', ('author', 'slug')]

# sections
# fieldsets = (
#     ('Section 1', {
#         'fields': ('title', 'author',),
#         'description': '%s' % TEXT,
#     }),
#     ('Section 2', {
#         'fields': ('slug',),
#         'classes': ('collapse',),
#     }),
# )


# admin.site.register(Post, PostAdmin)
