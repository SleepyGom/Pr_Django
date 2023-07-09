from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name='list'),
    path('create/', views.post_create, name='create'),
    path('<int:pk>/', views.post_detail, name='detail'),
    path('update/<int:pk>/', views.post_update, name='update'),
    path('delete/<int:pk>/', views.post_delete, name='delete'),
]