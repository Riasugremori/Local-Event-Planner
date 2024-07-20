from django.shortcuts import render, redirect, get_object_or_404
from .models import Event

def main_view(request):
    events = Event.objects.all()  
    return render(request, 'index.html', {'events': events})

def add_event_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        date = request.POST.get('date')
        location = request.POST.get('location')

        new_event = Event(
            title=title,
            description=description,
            date=date,
            location=location,
        )
        new_event.save()  
        return redirect('main')

    return render(request, 'add_event.html')

def event_detail(request, title):
    event = get_object_or_404(Event, title=title)
    return render(request, 'events.html', {'event': event})