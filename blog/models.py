from django.db import models


class BlogPost(models.Model):
    """ Blog post model """
    title = models.CharField(max_length=254, null=False, blank=False)
    preview = models.TextField(max_length=254, default='', blank=True)
    article = models.TextField(default='', blank=True)
    author = models.CharField(max_length=54, default='', blank=True)
    image = models.ImageField(null=True, blank=True)
    blog_source = models.CharField(max_length=254, blank=True, default='')
    source_url = models.URLField(max_length=1024, default='', blank=True)
    post_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title
