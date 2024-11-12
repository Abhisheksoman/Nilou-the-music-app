from django.urls import path
from music import views
from django.contrib import admin

urlpatterns =[
    path('admin/',admin.site.urls),
    path('', views.start, name='start'),
    path('home',views.home,name='home'),
    path('search_songs/', views.search_songs, name='search_songs'),
]