from django.contrib import admin

from .models import Booking



@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('user', 'name', 'contact_info', 'appointment_time', 'slots', 'appointment_type', 'is_booked')
    search_fields = ('appointment_type', 'contact_info')
    list_filter = ('is_booked',)
    