from django.shortcuts import render
from django.contrib import messages
from .models import Email

# Create your views here.
def home(request):
    # subscribe request, save the email in the database
    if "subscribe" in request.POST:
        if Email.objects.filter(email=request.POST["email"]).exists():
            messages.error(request, "You are already subscribed!")
        else:
            # Create a new instance of the model
            new_email = Email()
            # Set the email attribute to the email in the POST request
            new_email.email = request.POST['email']
            # Save the new email to the database
            new_email.save()
            messages.success(
                request, 'You have successfully subscribed to our newsletter.')

    if "unsubscribe" in request.POST:
        if Email.objects.filter(email=request.POST["email"]).exists():
            email = Email.objects.get(email=request.POST["email"])
            email.delete()
            messages.success(
                request, 'You have successfully unsubscribed from our newsletter.')
        else:
            messages.error(request, "You are not subscribed!")
    return render(request, 'home.html')
