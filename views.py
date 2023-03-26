# Create your views here.
from django.shortcuts import render, redirect
from .models import Event, Ticket

def event_list(request):
    events = Event.objects.all()
    return render(request, 'event_list.html', {'events': events})

def buy_ticket(request):
    event_id = request.GET.get('event_id')
    event = Event.objects.get(id=event_id)
    return render(request, 'buy_ticket.html', {'event': event})

def submit_ticket(request):
    if request.method == 'POST':
        event_id = request.POST.get('event_id')
        seat_number = request.POST.get('seat_number')
        price = request.POST.get('price')
        event = Event.objects.get(id=event_id)
        ticket = Ticket(event=event, seat_number=seat_number, price=price)
        ticket.save()
        return redirect('ticket_success')

def ticket_success(request):
    return render(request, 'ticket_success.html')
