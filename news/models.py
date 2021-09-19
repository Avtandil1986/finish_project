from django.db import models
from django.contrib.auth.models import User


def upload_to(instance, filename):
    return f'{filename}'


class News(models.Model):
    image = models.ImageField(upload_to=upload_to)
    title = models.TextField(max_length=100, null=True)
    data = models.DateTimeField(auto_now=True)
    short_text = models.CharField(max_length=1000)
    text = models.TextField()
    news = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Новости"


class ImageNews(models.Model):
    image = models.ImageField(upload_to=upload_to)
    news = models.ForeignKey(News, on_delete=models.CASCADE,
                             related_name="images")

    def __str__(self):
        return self.news.title

    class Meta:
        verbose_name = "Изображение для новости"


class Favourite(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.news.title

    class Meta:
        verbose_name = "Избранное Новостей"
