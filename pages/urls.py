from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),
    path('blog', views.blog, name='blog'),
    path('blog_detail/<int:id>', views.blog_detail, name='blog_detail'),
    path('contact', views.contact, name='contact'),
    path('post', views.post, name='post'),
    path('delete_blog/<int:id>', views.delete_blog, name='delete_blog'),
    path('edit_blog/<int:id>', views.edit_blog, name='edit_blog'),
    path('events', views.event, name='event'),
    path('likes', views.likes, name='likes'),
]

