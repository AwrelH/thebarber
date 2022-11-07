from urllib import request
from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.http import HttpResponse
from django.views import generic, View
from .models import Booking
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from .forms import AppointmentForm
from django.contrib import messages


def __init__(self, *args, **kwargs):
    super(Booking, self).__init__(*args, **kwargs)
    self.__original_mode = self.mode


def viewBooking(request, *args, **kwargs):
    bookings = Booking.objects.filter(user=request.user)
    context = {'bookings': bookings}
    return render(
        request, 'booking/booking.html', context
    )


def new_booking(request, *args, **kwargs):
    form = AppointmentForm()
    context = {'form': form}
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.instance.user = request.user
            form.save()
            messages.success(
                request, 'Thanks for your request, wait for confirmation')
            return redirect('booking')

    form = AppointmentForm()
    
    return render(
        request, 'booking/new_booking.html', context
    )


def edit_booking(request, pk, *args, **kwargs):
    appointment = Booking.objects.get(id=pk)

    form = AppointmentForm(instance=appointment)

    if request.method == 'POST':
        form = AppointmentForm(request.POST, instance=appointment)
        if form.is_valid():
            form.save()

            messages.success(
                request,
                'Your appointment has been changes, wait for new confirmation')
            return redirect('booking')

    context = {'form': form}
    return render(
        request,
        'booking/edit_booking.html', context
        )


def delete_booking(request, pk):
    appointment = Booking.objects.get(id=pk)

    if request.method == 'POST':
        appointment.delete()
        messages.success(
                request, 'Your appointment has been deleted')

        return redirect('booking')

    context = {'post': appointment}
    return render(
        request,
        'booking/delete_booking.html',
        context
        )
