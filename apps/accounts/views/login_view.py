from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib import messages
from accounts.forms import LoginForm
from accounts.services import AuthenticateUserService

def LoginView(request):
    if request.user.is_authenticated:
        if request.user.role == 'admin':
            return redirect('admin_panel:admin_dashboard')
        return redirect('customers:customer_panel')

    form = LoginForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']

            user = AuthenticateUserService(phone_number=phone_number, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "خوش آمدید!")
                
                if user.role == 'admin' or user.is_superuser:
                    return redirect('admin_panel:admin_dashboard') 
                return redirect('customers:customer_dashboard')
            else:
                messages.error(request, "شماره تماس یا رمز عبور اشتباه است.")
                return redirect('accounts:login')
        else:
            messages.error(request, "لطفاً اطلاعات ورودی را اصلاح کنید.")
            return redirect('accounts:login')

    return render(request, 'accounts/login.html', {'form': form})