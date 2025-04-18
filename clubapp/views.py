from django.shortcuts import render, get_object_or_404
from .models import Club, Event, Announcement
from datetime import date, timedelta
from django.shortcuts import render
from django.utils.timezone import now
from datetime import timedelta
from .models import Event
from django.shortcuts import render
from .models import Announcement

def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'clubapp/club_list.html', {'clubs': clubs})

def club_detail(request, id):
    club = get_object_or_404(Club, id=id)
    members = club.member_set.all()
    events = club.event_set.all()
    announcements = club.announcement_set.all()
    return render(request, 'clubapp/club_detail.html', {
        'club': club,
        'members': members,
        'events': events,
        'announcements': announcements
    })

def event_list(request):
    events = Event.objects.all()
    return render(request, 'clubapp/event_list.html', {'events': events})

def announcement_list(request):
    announcements = Announcement.objects.all()
    return render(request, 'clubapp/announcement_list.html', {'announcements': announcements})

def this_week_events(request):
    today = date.today()
    start_week = today - timedelta(days=today.weekday())  # Monday
    end_week = start_week + timedelta(days=6)  # Sunday
    events = Event.objects.filter(date__range=[start_week, end_week])
    return render(request, 'clubapp/this_week_events.html', {'events': events})

def home(request):
    return render(request, 'clubapp/home.html')

def this_week_events(request):
    today = now().date()
    week_end = today + timedelta(days=6)  # Next 6 days
    events = Event.objects.filter(date__range=[today, week_end])
    return render(request, "clubapp/this_week_events.html", {"events": events})

def announcement_list(request):
    announcements = Announcement.objects.all().order_by('-posted_on')  # Newest first
    return render(request, "clubapp/announcement_list.html", {"announcements": announcements})