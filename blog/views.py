""" Blog views.py """
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import BlogPost
from .forms import BlogForm


def all_posts(request):
    """ A view that returns all blog posts """
    posts = BlogPost.objects.all().order_by('-post_date')

    context = {
        'posts': posts,
    }

    return render(request, 'blog/blog.html', context)


def blog_detail(request, post_id):
    """ A view to return an individual blog posts details """
    post = get_object_or_404(BlogPost, pk=post_id)

    context = {
        'post': post,
    }

    return render(request, 'blog/blog_detail.html', context)


@login_required
def add_post(request):
    """ Add a blog post to blog page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, \
            only store owners are authorised to do that.')
        return redirect(reverse('home'))

    if request.method == 'POST':
        form = BlogForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()
            messages.success(request, f'Added {post.title} successfully!')
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
    """ Edit a blog post on the blog page """
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


@login_required
def delete_post(request, post_id):
    """ Delete a blog post on the blog page """
    if not request.user.is_superuser:
        messages.error(request, 'Sorry, \
            only store owners are authorised to do that.')
        return redirect(reverse('home'))

    post = get_object_or_404(BlogPost, pk=post_id)
    post.delete()
    messages.success(request, f'Blog post: {post.title} deleted!')
    return redirect(reverse('blog'))
