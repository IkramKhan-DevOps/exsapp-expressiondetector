from django.contrib import admin
from django.urls import path
from .views import HomeView, ImageListView

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('image/', ImageListView.as_view(), name='scan-image-list'),
]
