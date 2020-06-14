from django.contrib import admin
from datadesign.api.models import User, Event, Agent

# Register your models here.
admin.site.register(User)
admin.site.register(Agent)
admin.site.register(Event)
