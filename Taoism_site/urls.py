from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('shijie/', views.shijie, name='shijie'),
    path('service/', views.service, name='service'),
    path('contactus/', views.contactus, name='contactus'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('category/<str:category_name>/', views.category_posts, name='category_posts'),
    path('create/', views.create_post, name='create_post'),
    path('blogs/', views.blogs, name='blogs'),
    path('videos/', views.all_videos, name='all_videos'),
    path('videos/<str:category_name>/', views.category_videos, name='category_videos'),
]
