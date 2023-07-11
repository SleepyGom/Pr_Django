from django.urls import path , include
from . import views

app_name = 'blog'

urlpatterns = [
    # 글 목록 조회
    path('', views.home, name='home'),
    # 글 작성
    path('create/', views.post_create, name='create'),
    # 글 상세 조회
    path('<int:pk>/', views.post_detail, name='detail'),
    # 수정
    path('update/<int:pk>/', views.post_update, name='update'),
    # 삭제
    path('delete/<int:pk>/', views.post_delete, name='delete'),
    # auth
    path('auth/', include('django.contrib.auth.urls')),
    # 로그인
    path('login/', views.login_view, name='login')
]