from django.contrib import admin
from .models import Club, Member, Event, Announcement

admin.site.register(Club)
admin.site.register(Member)
admin.site.register(Event)
admin.site.register(Announcement)
