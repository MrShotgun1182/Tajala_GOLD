from django.urls import path
from customers import views

app_name = 'customers'

urlpatterns = [
    path('', views.CustomerDashboardView, name='customer_dashboard'),
    path('showcase/', views.CustomerShowcaseView, name='showcase'),
    path('product/<slug:slug>/', views.ProductDetailView, name='product_detail'),
]