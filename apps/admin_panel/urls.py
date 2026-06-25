from django.urls import path
from admin_panel import views

app_name = 'admin_panel'

urlpatterns = [
    path('dashboard/', views.AdminDashboardView, name='admin_dashboard'),
    path('transactions_history/', views.AdminTransactionHistoryView, name='transactions_history'),
    path('products_list/', views.AdminProductListView, name='products_list'),
    path('create_gold_transaction/', views.GoldTransactionView, name='create_gold_transaction'),
    path('api/search/', views.AdminCustomerSearchApi, name='search_api'),
    path('create_product/', views.AdminCreateProductView, name='create_product'),
]