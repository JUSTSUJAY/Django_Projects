from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    class Meta:
        model = Event
        fields = ['name', 'event_time']
        widgets = {
            'event_time': forms.DateInput(attrs={'class': 'form-control datepicker', 'placeholder': 'Select a date'}),
        }
