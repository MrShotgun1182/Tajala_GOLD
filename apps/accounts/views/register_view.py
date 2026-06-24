from django.shortcuts import render, redirect
from django.contrib import messages
from accounts import forms
from accounts import services

def RegisterView(request):
    """
    ویو اختصاصی برای ثبت‌نام اولیه مشتری در سامانه تجلا؛
    مدیریت نمایش فرم و اتصال معتبرسازی فرم به لایه سرویس خالص.
    """
    # ۱. پردازش درخواست ثبت‌نام (ارسال فرم)
    if request.method == 'POST':
        form = forms.RegisterForm(request.POST)
        if form.is_valid():
            # استخراج داده‌های معتبرسازی شده از فرم
            phone_number = form.cleaned_data['phone_number']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            
            try:
                # فراخوانی لایه سرویس برای ایجاد تراکنشی کاربر و مشتری
                services.CreateCustomerService(
                    phone_number=phone_number,
                    password=password,
                    first_name=first_name,
                    last_name=last_name
                )
                messages.success(request, "حساب کاربری شما با موفقیت در سامانه تجلا ایجاد شد. اکنون می‌توانید وارد شوید.")
                return redirect('customers:customer_dashboard') # فرض بر اینکه نام روت لاگین این است
                
            except Exception as e:
                # مدیریت خطاهای غیرمنتظره دیتابیس
                form.add_error(None, "خطایی در ذخیره‌سازی اطلاعات رخ داده است. لطفا مجددا تلاش کنید.")
    
    # ۲. پردازش درخواست نمایش صفحه (GET)
    else:
        form = forms.RegisterForm()

    context = {
        'form': form
    }
    
    # ارجاع به تمپلیت اختصاصی اپلیکیشن با الگوی Namespace برای جلوگیری از تداخل
    return render(request, 'accounts/register.html', context)