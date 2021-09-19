"""django_finish_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from news import views

urlpatterns = [

    path('admin/',admin.site.urls),
    path("api/v1/news/",views.NewsListApiView.as_view()),
    path("api/v1/news/<int:pk>/",views.NewsItemApiView.as_view()),
    path("api/v1/newsfavourites/",views.favourites),
    path("api/v2/newswitsfavorites/",views.news_with_favourite),

    path("api/v1/law/",include("project.urls")),
    path("api/v1/library/",include("nco.urls")),
    path("api/v1/account/",include("users.urls")),

]
urlpatterns += static(settings.MEDIA_URL,
                      document_root=settings.MEDIA_ROOT)
