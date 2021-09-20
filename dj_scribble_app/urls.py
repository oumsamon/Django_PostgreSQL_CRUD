from django.urls import path

from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('comment/', views.comment_list, name='comment_list'),
]