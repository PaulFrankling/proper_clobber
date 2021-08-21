from django.db import models


class BlogPost(models.Model):

    title = models.CharField(max_length=254, null=False, blank=False)
    preview = models.TextField(max_length=254, null=True, blank=True)
    article = models.TextField(null=True, blank=True)
    author = models.CharField(max_length=54, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)
    blog_source = models.CharField(max_length=254, blank=True, null=True)
    source_url = models.URLField(max_length=1024, null=True, blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
