from django.contrib import admin
from .models import BlogPost


class BlogAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'preview',
        'article',
        'author',
        'post_date',
        'image',
    )


admin.site.register(BlogPost, BlogAdmin)
