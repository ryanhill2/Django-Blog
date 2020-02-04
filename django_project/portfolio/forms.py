from django import forms
from django.utils.safestring import mark_safe
from .models import stock

class stockForm(forms.ModelForm):
    stock_ticker = forms.CharField(label='Stock Ticker')
    purchase_price = forms.CharField(label='Purchase Price')
    number_of_shares = forms.CharField(label='Number of Shares')

    class Meta:
        model = stock
        fields = ('stock_ticker', 'purchase_price', 'number_of_shares',)
