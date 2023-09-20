from django.urls import path
from . import views

app_name = 'myapp'

urlpatterns = [
    path("", views.home, name="home"),
    path('post/', views.post, name='post'),
    path('author/', views.author, name='author'),
    path('create_post/', views.create_post, name='create_post'),
    path('detail/<int:post_id>/', views.detail, name='detail'),
]