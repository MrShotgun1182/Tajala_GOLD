from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('dashboard/', views.AdminDashboardView, name='admin_dashboard'),
    path('transactions_history/', views.AdminTransactionHistoryView, name='transactions_history'),
    path('products_list/', views.AdminProductListView, name='products_list'),
    path('gold-transactions/create/', views.GoldTransactionView, name='create_gold_transaction'),
    path('api/search/', views.AdminCustomerSearchApi, name='search_api'),
    
]