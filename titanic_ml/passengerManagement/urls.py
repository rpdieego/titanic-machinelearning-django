from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='pM_home'),
    path('delete/<list_id>', views.delete, name='delete'),
    path('posts/<str:pk_test>/', views.posts, name='posts'),

]
