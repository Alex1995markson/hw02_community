from django.shortcuts import render, get_object_or_404


from .models import Post, Group


def index(request):
    posts = Post.objects.select_related('author') \
                .select_related('group')
    return render(request, 'index.html', {"posts": posts})


def group_posts(self, slug):
    group = get_object_or_404(Group, slug=slug)
    posts = Post.objects.filter(group=group).order_by("-pub_date")[:12]
    return render(Group, "group.html", {"group": group, "posts": posts})
