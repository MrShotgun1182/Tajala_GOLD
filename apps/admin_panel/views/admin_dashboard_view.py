from django.shortcuts import render
from django.contrib.auth.decorators import login_required

@login_required
def AdminDashboardView(request):
    return render(request, 'admin_panel/admin_dashboard.html')