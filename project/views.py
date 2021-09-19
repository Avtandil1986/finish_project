from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import generics
from project.models import ProjectFavourite, LawAllNCO
from project.serializers import LawSerializers, ProjectFavouriteSerializers, ProjectWithFavouriteSerializers, \
    LawCategorySerializers


class LawAllApiView(generics.ListAPIView):
    queryset = LawAllNCO.objects.all()
    serializer_class = LawSerializers


class LawAllCategoryApiView(generics.ListAPIView):
    queryset = LawAllNCO.objects.all()
    serializer_class = LawCategorySerializers


@permission_classes(IsAuthenticated)
@api_view(["GET", "POST", "DELETE"])
def law_favourites(request):
    if request.method == "GET":
        favourites_list = ProjectFavourite.objects.filter(user=request.user)
        data = ProjectFavouriteSerializers(favourites_list, many=True).data
        return Response(data=data)
    elif request.method == "POST":
        project_id = request.data["project_id"]
        ProjectFavourite.objects.create(project_id=project_id,
                                        user=request.user)
        return Response(data={"message": "Favourite created!!!!"})
    elif request.method == "DELETE":
        project_id = request.data["project_id"]
        ProjectFavourite.objects.filter(project_id=project_id,
                                        user=request.user).delete()

        return Response(data={"message": "Favourite removed!!!!"})


@api_view(["GET"])
def law_with_favourite(request):
    project = LawAllNCO.objects.all()
    data = ProjectWithFavouriteSerializers(project, many=True, context={"request": request}).data

    return Response(data=data)
