from django.db import models
from django.contrib.auth.models import User


TIMESLOTS = {
    (10, '10:00'),
    (11, '11:00'),
    (12, '12:00'),
    (13, '13:00'),
    (14, '14:00'),
    (15, '15:00'),
    (16, '16:00'),
    (17, '17:00'),
    (18, '18:00')
}


class Booking(models.Model):

    user = models.ForeignKey(
        User, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=True, blank=True)
    contact_info = models.TextField(null=False, blank=False)
    appointment_type = models.IntegerField(
        default=1,
        choices=(
            (1, 'Haircut'), (2, 'Beard Grooming'), (3, 'Haircut & Beard')))
    appointment_time = models.DateField(null=False, blank=False)
    slots = models.IntegerField(choices=TIMESLOTS, default='10')
    is_booked = models.BooleanField(default=False)

    class Meta:
        ordering = ['-appointment_time']
        constraints = [
            models.UniqueConstraint(
                fields=[
                    'appointment_time',
                    'slots'], name='no_double_booking')]

    def __str__(self):
        return self.name
