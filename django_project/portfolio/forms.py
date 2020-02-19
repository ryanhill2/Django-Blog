from django import forms
from django.utils.safestring import mark_safe
from .models import Stock, Portfolio


class stockForm(forms.ModelForm):
    stock_ticker = forms.CharField(label='Stock Ticker')
    number_of_shares = forms.CharField(label='Number of Shares')

    class Meta:
        model = Stock
        fields = ('stock_ticker', 'number_of_shares',)


class portfolioForm(forms.ModelForm):
    portfolio_name = forms.CharField(label='Portfolio Name')

    class Meta:
        model = Portfolio
        fields = ('portfolio_name',)
