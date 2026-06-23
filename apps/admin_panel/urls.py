from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', views.AdminDashboardView, name='admin_dashboard'),
    path('transactions_history/', views.AdminTransactionHistoryView, name='transactions_history'),
    # path(),
    
]