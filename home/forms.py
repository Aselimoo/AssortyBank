from .models import UserProfile, Transaction
from django.forms import ModelForm

class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = ['sender', 'recipient', 'summa']
        widgets = {}