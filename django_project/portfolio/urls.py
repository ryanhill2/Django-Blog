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
    path('view_portfolio/', views.viewPortfolio, name='portfolio-view-portfolio'),
    path('create_portfolio/', views.addportfolio.as_view(), name='portfolio-create-portfolio'),
    path('advanced_analysis/', views.advanced_analysis, name='portfolio-advanced-analysis'),
]

