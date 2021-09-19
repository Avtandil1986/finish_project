from django.urls import path
from project import views

urlpatterns = [
    path("legislations_nco/", views.LawAllApiView.as_view()),
    path("categotylaw/", views.LawAllCategoryApiView.as_view()),
    path("lawfavorites/", views.law_favourites),
    path("lawwithfavourite/", views.law_with_favourite)

]
