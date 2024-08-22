from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user = models.ForeignKey(User, on_delete = models.CASCADE)
    recipe_name = models.CharField(max_length=100)
    recipe_decription = models.TextField()
    recipe_image = models.ImageField(upload_to = "images/")
    def __str__(self):
        return self.recipe_name
