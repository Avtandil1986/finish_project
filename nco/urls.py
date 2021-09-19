from django.urls import path
from nco import views

urlpatterns = [
    path("nco/", views.NCOAllApiView.as_view()),
    path("ncocategory/", views.NCOCategoryAllApiView.as_view()),
    path("ncofavorites/", views.nco_favourites),
    path("ncowithfavourite/", views.nco_with_favourite),

]
