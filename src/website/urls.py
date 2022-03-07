from django.contrib import admin
from django.urls import path
from .views import HomeView, ImageListView, ImageDetailView

app_name = 'website'
urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('image/', ImageListView.as_view(), name='scan-image-list'),
    path('image/<int:pk>/', ImageDetailView.as_view(), name='scan-image-detail'),
]
