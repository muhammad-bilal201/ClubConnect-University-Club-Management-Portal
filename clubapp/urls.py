from django.urls import path
from . import views

"""urlpatterns = [
    path('', views.home, name='home'),  # Homepage
    path('clubs/', views.club_list, name='club_list'),
    path('clubs/<int:id>/', views.club_detail, name='club_detail'),
    path('events/', views.event_list, name='event_list'),
    path('announcements/', views.announcement_list, name='announcement_list'),
    path('this-week/', views.this_week_events, name='this_week_events'),
]
"""
from django.urls import path
from . import views

urlpatterns = [
    path("clubs/", views.club_list, name="club_list"),
    path("clubs/<int:id>/", views.club_detail, name="club_detail"),
    path("events/", views.event_list, name="event_list"),
    path("announcements/", views.announcement_list, name="announcement_list"),
    path("this-week/", views.this_week_events, name="this_week_events"),  # ✅ Fix added here
]

