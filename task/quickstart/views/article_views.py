from django.db.models import manager
from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.response import Response

from quickstart.models import Article
from quickstart.serializers import ArticleSerializer
   
from rest_framework import serializers, status
from datetime import datetime




@api_view(['GET'])
def getArticles(request):
    articles = Article.objects.all()
    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getArticleById(request, pk):    
    try:  
        article = Article.objects.get(_id=pk)
        serializer = ArticleSerializer(article, many=False)
        return Response(serializer.data)
    except:
        return Response({'detail': 'Article does not exists'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def addArticle(request):
    try:
        user = request.user
        data = request.data
        print(user)
    
        order = Article.objects.create(
                                    author = user,
                                    title = data['title'],
                                    description = data['description']
                                )
        
        serializer = ArticleSerializer(order, many=False)
        return Response(serializer.data)

    except:
        return Response({'detail': 'Something went wrong'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def updateArticle(request, pk):
    user = request.user
    data = request.data

    try:  
        article = Article.objects.get(_id=pk)
        if user.is_staff or article.author==user:
            article.title = data['title']
            article.description = data['description']
            # article.modifiedAt = datetime.now()
            article.save()

            serializer = ArticleSerializer(article, many=False)
            return Response(serializer.data)

        else:
            return Response({'detail': 'Not authorized to edit this article'}, status=status.HTTP_400_BAD_REQUEST)

    except:
        return Response({'detail': 'Article does not exists'}, status=status.HTTP_400_BAD_REQUEST)



@api_view(['DELETE'])
@permission_classes([IsAdminUser])
def deleteArticle(request, pk):
    user = request.user
    try:
        article = Article.objects.get(_id=pk)
        if user.is_staff or article.author==user:
            article.delete()
            return Response('Article Deleted')
        else:
            return Response({'detail': 'Not authorized to edit this article'}, status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response({'detail': 'Article does not exists'}, status=status.HTTP_400_BAD_REQUEST)