from user import views
from django.urls import path
from django.contrib import admin

urlpatterns = [
    path('admin/',admin.site.urls),
    path('register/', views.register, name='register'),
    path('login_view/', views.login_view, name='login_view'),
    path('show', views.show, name='show'),
    path('forget_password/', views.forget_password, name='forget_password'),
    path('delete', views.delete, name='delete'),
    path('update/', views.update, name='update'),
    path('logout', views.user_logout, name='user_logout'),
]