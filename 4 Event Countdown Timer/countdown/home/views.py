from django.shortcuts import render, redirect
from django.utils import timezone
from .models import Event
from .forms import EventForm

# Create your views here.
def home(request):
    first_event = Event.objects.first()
    if first_event: # if the event has been succesffuly retrieved from database
        time_remaining = first_event.event_time - timezone.now()
        hours = time_remaining.seconds // 3600
        minutes = (time_remaining.seconds % 3600) // 60
        seconds = time_remaining.seconds % 60
        data = {
            'event_name' : first_event.name,
            'hours':hours,
            'minutes':minutes,
            'seconds':seconds,
        }
    else:
        data = {
            'event_name' : 'No Event',
            'hours':0,
            'minutes':0,
            'seconds':0,
        }


    return render(request, 'home.html', {'data':data})


def event_create(request):
    if request.method == 'POST':
        form = EventForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = EventForm()
    return render(request, 'event_create.html', {'form':form})