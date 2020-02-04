from django import forms
from django.utils.safestring import mark_safe

class stockForm(forms.Form):
    stock_ticker = forms.CharField(label='Stock Ticker')
    purchase_price = forms.CharField(label='Purchase Price')
    number_of_shares = forms.CharField(label='Number of Shares')
