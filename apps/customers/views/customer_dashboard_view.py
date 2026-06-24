from django.shortcuts import render

def CustomerDashboardView(request):
    return render(request, 'customers/customer_dashboard.html')