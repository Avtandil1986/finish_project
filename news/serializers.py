from rest_framework import serializers

from .models import News, ImageNews, Favourite


class NewsListSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = "id image title data short_text  ".split()


class ImageNewsSerializers(serializers.ModelSerializer):
    class Meta:
        model = ImageNews
        fields = "id image".split()


class NewsObjectSerializers(serializers.ModelSerializer):
    images = ImageNewsSerializers(many=True)

    class Meta:
        model = News
        fields = "id image title text news images".split()



class FavouriteSerializers(serializers.ModelSerializer):
    news = NewsListSerializer

    class Meta:
        model = Favourite
        fields = "__all__"


class NewsWithFavouriteSerializers(serializers.ModelSerializer):
    is_favourite = serializers.SerializerMethodField()

    class Meta:
        model = News
        fields = "id title is_favourite".split()

    def get_is_favourite(self, news):
        request = self.context["request"]
        return bool(request.user.is_authenticated
                    and Favourite.objects.filter(user=request.user, news=news).count() > 0)
