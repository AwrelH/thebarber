from django.contrib import admin
from .models import VisitorMessage


@admin.register(VisitorMessage)
class UserMessage(admin.ModelAdmin):
    list_display = ('name', 'question', 'email', 'created_on')


