from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from .views import Blogviewset
from django.contrib.auth import views as auth_views
router=DefaultRouter()
router.register('blogs', views.Blogviewset, basename='blog')
urlpatterns = [
    path('', views.index, name='index'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('delete/<int:pk>/', views.delete_post, name='delete_post'),
    path('api/', include(router.urls)),
    path('login/', auth_views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]