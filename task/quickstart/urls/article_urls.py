from django.urls import path
from quickstart.views import article_views as views



urlpatterns = [
    path('add/', views.addArticle, name='add-article'),
    path('<str:pk>/', views.getArticleById, name='view-article-id'),
    path('', views.getArticles, name='view-article'),

    path('update/<str:pk>/', views.updateArticle, name='update-article'),
    path('delete/<str:pk>/', views.deleteArticle, name='delete-article'),
]