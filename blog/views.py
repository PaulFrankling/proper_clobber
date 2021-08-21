from django.shortcuts import render
from .models import BlogPost


def all_posts(request):
    posts = BlogPost.objects.all().order_by('-post_date')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)
