from django.urls import path
from . import views

urlpatterns = \
    [
        path('', views.show_posts, name='index'),
        path('index', views.show_posts, name='index'),
        path('login', views.login_view, name='login'),
        path('register', views.register, name='register'),
        path('logout', views.logout, name='logout'),
        path('post', views.show_posts, name='show_posts'),
        path('create_post', views.create_post, name='create_post'),
    ]
