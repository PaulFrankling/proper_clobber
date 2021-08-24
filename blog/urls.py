from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_posts, name='blog'),
    path('<int:post_id>/', views.blog_detail, name='blog_detail'),
    path('add/', views.add_post, name='add_post'),
]
