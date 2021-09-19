from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from news.serializers import *
from rest_framework import generics

from news.models import News, Favourite


class NewsListApiView(generics.ListAPIView):
    queryset = News.objects.all()
    serializer_class = NewsListSerializer


class NewsItemApiView(generics.RetrieveAPIView):
    queryset = News.objects.all()
    serializer_class = NewsObjectSerializers


@permission_classes(IsAuthenticated)
@api_view(["GET", "POST", "DELETE"])
def favourites(request):
    if request.method == "GET":
        favourites_list = Favourite.objects.filter(user=request.user)
        data = FavouriteSerializers(favourites_list, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        news_id = request.data["news_id"]
        Favourite.objects.create(news_id=news_id,
                                 user=request.user)
        return Response(data={"message": "Favourite created!!!!"})
    elif request.method == "DELETE":
        news_id = request.data["news_id"]
        Favourite.objects.filter(news_id=news_id,
                                 user=request.user).delete()

        return Response(data={"message": "Favourite removed!!!!"})


@api_view(["GET"])
def news_with_favourite(request):
    news = News.objects.all()
    data = NewsWithFavouriteSerializers(news, many=True, context={"request": request}).data

    return Response(data=data)
