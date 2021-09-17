from django.http.response import HttpResponse
from django.shortcuts import render

from .models import Post


def blog(request):
    posts = Post.objects.all()

    return render(request, 'blog/home.html', {'posts': posts})
