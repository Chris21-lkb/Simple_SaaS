from django.urls import path
from . import views

app_name = 'link'

urlpatterns = [
    path('categories/create-category/', views.create_category, name='create_category'),
    path('create-link/', views.create_link, name='create_link'),
    path('categories/', views.categories, name='categories'),
    path('categories/<int:pk>/edit/', views.edit_category, name='edit_category'),
    path('categories/<int:pk>/delete/', views.delete_category, name='delete_category'),
    path('<int:pk>/edit/', views.edit_link, name='edit_link'),
    path('<int:pk>/delete/', views.delete_link, name='delete_link'),
    path('', views.links, name='links'),
]