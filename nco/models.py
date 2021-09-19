from django.db import models
from rest_framework.authtoken.admin import User


class NCOCategory(models.Model):
    category = models.CharField(max_length=300, verbose_name="Название категории библиотеки")

    class Meta:
        verbose_name = "Библиотека НCО "

    def __str__(self):
        return f'{self.category}'


class PublicationNCO(models.Model):
    time = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=200, verbose_name="Заголовок публикации ")
    all_text = models.TextField(null=True, verbose_name="Описание публикации")

    category = models.ForeignKey(NCOCategory, on_delete=models.CASCADE, null=True)

    class Meta:
        verbose_name = "Публикации INCL"

    def __str__(self):
        return f'{self.category}'


class PublicationFavourite(models.Model):
    public = models.ForeignKey(PublicationNCO, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Избранное публикации  "

    def __str__(self):
        return self.public.title
