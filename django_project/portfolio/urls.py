from django.urls import path
from .import views

from .views import (
    TransactionPageView,
)


urlpatterns = [
    path('', views.portfolio, name='portfolio-portfolio'),
    # path('', views.portfolio.as_view(), name='portfolio-portfolio'),
    path('addstock/', views.addstock.as_view(), name='portfolio-addstock'),
    path('transaction_page/', TransactionPageView.as_view(), name='portfolio-transaction-page'),
]

