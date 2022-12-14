from django.db import models

# Create your models here.


class VisitorMessage(models.Model):
    name = models.CharField(max_length=50)
    question = models.TextField(max_length=200)
    email = models.EmailField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return f'{self.name} has left a message'
