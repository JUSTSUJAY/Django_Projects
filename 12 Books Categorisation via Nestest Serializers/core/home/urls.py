from django.urls import path
from . import views
urlpatterns = [
    path('get-book', views.get_book, name='get_book'),
]

