from django.shortcuts import render, get_object_or_404

from .models import Post, Group


def index(request):
    posts = Post.objects.all()[:10]
    return render(request, 'index.html', {"posts": posts})


def group_posts(request, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()[:10]
    return render(request, "group.html", {"group": group, "posts": posts})
