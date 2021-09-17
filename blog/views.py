from django.shortcuts import render

from .models import Post


def home(request):
    qs = Post.objects.all()
    return render(request, 'blog/home.html', {'qs': qs})
