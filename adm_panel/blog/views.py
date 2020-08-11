from django.shortcuts import render, get_object_or_404
from .models import Post
from django.utils import timezone


def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/posts_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)  # pk - это personal key. Если ты его не заводил в БД, то Django завел его сам
    return render(request, 'blog/post_detail.html', {'post': post})