from django.forms import ModelForm
from .models import Transactions

class TransactionsForm(ModelForm):
    class Meta:
        model = Transactions
        fields = ('data', 'description', 'value', 'notes', 'category')
