from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.post_main, name='post_main'),
    #path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/',views.post_new, name='post_new'),
    path('post/<int:pk>/edit/',views.post_edit, name='post_edit'),
    path('post/<int:pk>/delete/',views.post_delete,name='post_delete'),
    path('post/<int:pk>/auth',views.post_auth,name='post_auth'),
]