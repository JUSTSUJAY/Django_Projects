from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    image = models.ImageField(upload_to='products/')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    def edit(self,name, description,image):
        self.name = name
        self.description = description
        self.image = image
        self.save()

    def short_description(self):
        # The function to make sure that in the display only 50 words are present
        words = self.description.split()
        if len(words) > 50:
            return ' '.join(words[0:50]) + '...'
        else:
            return self.description # description already has less that 50 words

            


