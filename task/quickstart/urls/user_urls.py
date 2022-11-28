from django.urls import path
from quickstart.views import user_views as views
from rest_framework.permissions import SAFE_METHODS



urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(), name='token_obtain_pair'), 
    path('register/', views.registerUser, name='register'), 

    path('profile/', views.getUserProfile, name='users-profile'), 
    
    path('', views.getUsers, name='users'),
    path('<str:pk>/', views.getUserById, name='user'),

    path('update/<str:pk>/', views.updateUser, name='user-update'),
    path('delete/<str:pk>/', views.deleteUser, name='user-delete'),
]