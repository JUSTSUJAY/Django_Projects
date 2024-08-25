from django.shortcuts import render
from .forms import ContactForm
from django.http import HttpResponse

# Create your views here.
def contact(request):
    if request.method == "POST":
        form_received = ContactForm(request.POST)
        if form_received.is_valid():
            return HttpResponse("Thank you for your message.")
        else:
            return HttpResponse("Something went wrong.")
    else:
        form = ContactForm()

    return render(request, "contact.html", {"form": form})

