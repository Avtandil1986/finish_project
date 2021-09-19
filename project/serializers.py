from rest_framework import serializers
from project.models import ProjectFavourite, NCOCategory, LawAllNCO


class LawSerializers(serializers.ModelSerializer):
    class Meta:
        model = LawAllNCO
        fields = "__all__"


class LawCategorySerializers(serializers.ModelSerializer):
    class Meta:
        model = NCOCategory
        fields = "id category  ".split()


class ProjectFavouriteSerializers(serializers.ModelSerializer):
    Project = LawSerializers

    class Meta:
        model = ProjectFavourite
        fields = "__all__"


class ProjectWithFavouriteSerializers(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = LawAllNCO
        fields = "id title is_favourite".split()

    def get_is_favourite(self, project):
        request = self.context["request"]
        return bool(request.user.is_authenticated
                    and ProjectFavourite.objects.filter(user=request.user, project=project).count() > 0)
