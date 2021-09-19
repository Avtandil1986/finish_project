from rest_framework import serializers
from nco.models import *


class NCOSerializers(serializers.ModelSerializer):
    class Meta:
        model = PublicationNCO
        fields = "__all__"


class CategoryNCOSerializers(serializers.ModelSerializer):
    class Meta:
        model = NCOCategory
        fields = "__all__"


class PublicationFavouriteSerializers(serializers.ModelSerializer):
    nco = NCOSerializers

    class Meta:
        model = PublicationFavourite
        fields = "__all__"


class PublicWithFavouriteSerializers(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = PublicationNCO
        fields = "id title is_favourite".split()

    def get_is_favourite(self, public):
        request = self.context["request"]
        return bool(request.user.is_authenticated
                    and PublicationFavourite.objects.filter(user=request.user, public=public).count() > 0)
