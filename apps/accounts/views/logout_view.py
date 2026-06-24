from django.shortcuts import redirect
from django.contrib.auth import logout


def LogoutView(request):
    if request.user.is_authenticated:
        logout(request)
    
    return redirect('core:landing')