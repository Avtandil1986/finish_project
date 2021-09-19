from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from nco.serializers import *


class NCOAllApiView(generics.ListCreateAPIView):
    queryset = PublicationNCO.objects.all()
    serializer_class = NCOSerializers


class NCOCategoryAllApiView(generics.ListAPIView):
    queryset = PublicationNCO.objects.all()
    serializer_class = CategoryNCOSerializers


@permission_classes(IsAuthenticated)
@api_view(["GET", "POST", "DELETE"])
def nco_favourites(request):
    if request.method == "GET":
        favourites_list = PublicationFavourite.objects.filter(user=request.user)
        data = PublicationFavouriteSerializers(favourites_list, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        public_id = request.data["public_id"]
        PublicationFavourite.objects.create(public_id=public_id,
                                            user=request.user)
        return Response(data={"message": "Favourite created!!!!"})
    elif request.method == "DELETE":
        public_id = request.data["public_id"]
        PublicationFavourite.objects.filter(public_id=public_id,
                                            user=request.user).delete()

        return Response(data={"message": "Favourite removed!!!!"})


@api_view(["GET"])
def nco_with_favourite(request):
    public = PublicationNCO.objects.all()
    data = PublicWithFavouriteSerializers(public, many=True, context={"request": request}).data

    return Response(data=data)
