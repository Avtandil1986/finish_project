from django.db import models
from rest_framework.authtoken.admin import User


class NCOCategory(models.Model):
    category = models.CharField(max_length=300, verbose_name="Название законодательство")

    class Meta:
        verbose_name = "Законодательство об НCО"

    def __str__(self):
        return f'{self.category}'


class LawAllNCO(models.Model):
    title = models.CharField(max_length=1000, null=True,
                             verbose_name="Название закона")
    all_text = models.TextField(null=True, verbose_name="Описание закона")

    category = models.ForeignKey(NCOCategory, on_delete=models.CASCADE, null=True, verbose_name="Категория")

    class Meta:
        verbose_name = "Законы"

    def __str__(self):
        return self.title


class ProjectFavourite(models.Model):
    ProjectFavourite = models.ForeignKey(LawAllNCO, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Избранное законов "

    def __str__(self):
        return self.ProjectFavourite.title
#
# LAW_TYPES = (
#     (1, "Действующее законодательство"),
#     (2, "Проекты"),
#     (2, "Действующие документы")

