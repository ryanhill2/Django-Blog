from django.urls import path
from .import views

urlpatterns = [
    path('', views.portfolio, name='portfolio-portfolio'),
    # path('', views.portfolio.as_view(), name='portfolio-portfolio'),
    path('addstock/', views.addstock.as_view(), name='portfolio-addstock')
]

