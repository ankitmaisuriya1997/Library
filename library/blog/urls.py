from django.urls import path, include
from blog import views

urlpatterns = [
    path('library/', views.Library, name='Library'),
    path('createLibrary/', views.createLibrary, name='createLibrary'),
]