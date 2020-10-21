from django.contrib import admin
from django.contrib.admin import AdminSite

from .models import Category, Origin, Hero, Villain

class EventAdminSite(AdminSite):
    site_header = "UMSRA Events Admin"
    site_title = "UMSRA Events Admin Portal"
    index_title = "Welcome to UMSRA Researcher Events Portal"


events_admin_site = EventAdminSite(name='event_admin')

