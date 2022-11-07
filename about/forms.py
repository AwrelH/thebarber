from .models import VisitorMessage
from django import forms


class MessageForm(forms.ModelForm):
    class Meta:
        model = VisitorMessage
        fields = ('name', 'question', 'email')

        labels = {
            'name': 'Name',
            'question': 'Question or feedback'
        }
        widgets = {
            'name': forms.TextInput(
                attrs={'placeholder': 'George Costanza'}),
            'question': forms.Textarea(
                attrs={'placeholder': 'Example question...'}),
            'email': forms.EmailInput(
                attrs={'placeholder': 'email@example.com'})
        }
