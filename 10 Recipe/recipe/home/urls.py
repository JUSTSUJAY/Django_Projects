from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create", views.create_recipe, name="create_recipe"),
    path("<int:recipe_id>/edit/", views.edit_recipe, name="edit_recipe"),
    path("<int:recipe_id>/delete/", views.delete_recipe, name="delete_recipe"),
    path("register/", views.register, name="register"),
]