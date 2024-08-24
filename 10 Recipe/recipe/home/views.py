from django.shortcuts import render
from .models import Recipe
from .forms import RecipeForm, UserRegistrationForm
from django.shortcuts import redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
# Create your views here.
def home(request):
    recipes = Recipe.objects.all()
    return render(request, 'home/home.html', {"recipes": recipes})

@login_required
def create_recipe(request):
    if request.method == "POST":
        recieved_form = RecipeForm(request.POST, request.FILES)
        if recieved_form.is_valid():
            recipe = recieved_form.save(commit = False)
            recipe.user = request.user
            recipe.save()
            return redirect('home')
    else:
        form_distribute = RecipeForm()
        return render(request, 'home/create_recipe.html', {"form": form_distribute})

@login_required
def edit_recipe(request, recipe_id):
    recipe_to_be_edited = get_object_or_404(Recipe, pk = recipe_id, user = request.user)
    if request.method == "POST":
        received_form = RecipeForm(request.POST, request.FILES, instance = recipe_to_be_edited)
        if received_form.is_valid():
            recipe = received_form.save(commit = False)
            recipe.user = request.user
            recipe.save()
            return redirect('home')
    else:
        form_distribute = RecipeForm(instance = recipe_to_be_edited)
    return render(request, 'home/create_recipe.html', {"form": form_distribute})

@login_required
def delete_recipe(request, recipe_id):
    recipe_to_be_deleted = get_object_or_404(Recipe, pk = recipe_id, user = request.user)
    if request.method == "POST":
        recipe_to_be_deleted.delete()
        return redirect('home')
    return render(request, 'home/delete_recipe.html', {"recipe": recipe_to_be_deleted})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit = False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('login')
    else:
        form = UserRegistrationForm()
    return render(request, 'registration/register.html', {'form' : form})