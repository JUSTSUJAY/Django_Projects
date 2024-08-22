from django.shortcuts import render
from .models import Recipe

# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home/home.html', {"recipes": recipes})
