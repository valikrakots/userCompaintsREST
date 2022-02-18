from django.contrib import admin

# Register your models here.
from ticket.models import Ticket

admin.site.register(Ticket)