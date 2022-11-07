from django.shortcuts import render
from urllib import request
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse
from django.views import generic, View
from .models import VisitorMessage
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import MessageForm
from django.contrib import messages


def about(request):
    form = MessageForm()
    context = {
        'form': form
        }

    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(
                request, 'Your message has been received')

    
    return render(
        request,
        'about/about.html', context
        )

