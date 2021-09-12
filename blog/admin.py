""" Blog admin.py """
from django.contrib import admin
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    """ Admin display for blog post """
    list_display = (
        'title',
        'preview',
        'article',
        'author',
        'post_date',
        'image',
    )


admin.site.register(BlogPost, BlogAdmin)
