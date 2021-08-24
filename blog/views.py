from django.shortcuts import render, redirect, reverse, get_object_or_404
from .models import BlogPost
from .forms import BlogForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


def all_posts(request):
    posts = BlogPost.objects.all().order_by('-post_date')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, post_id):
    post = get_object_or_404(BlogPost, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_post(request):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, \
            only store owners are authorised to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, 'Added Post successfully!')
            return redirect(reverse('blog_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to add post. \
                Please ensure the form is valid.')
    else:
        form = BlogForm()

    form = BlogForm()
    context = {
        'form': form,
    }

    return render(request, 'blog/add_post.html', context)


@login_required
def edit_post(request, post_id):
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, \
            only store owners are authorised to do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(BlogPost, pk=post_id)
    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Updated Post Successfully!')
            return redirect(reverse('blog_detail', args=[post.id]))
        else:
            messages.error(request, 'Failed to update post. \
                Please ensure the form is valid.')
    else:
        form = BlogForm(instance=post)
        messages.info(request, f'You are editing the post: {post.title}')

    context = {
        'form': form,
        'post': post,
    }

    return render(request, 'blog/edit_post.html', context)
