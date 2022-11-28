# from quickstart.settings import MEDIA_ROOT
import quickstart
from django.contrib import admin
from django.urls import path, include

from django.conf import Settings, settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/users/', include('quickstart.urls.user_urls')),
    path('api/articles/', include('quickstart.urls.article_urls')),
]