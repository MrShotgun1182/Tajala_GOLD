from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ValidationError
from admin_panel import forms
from transactions import services

def GoldTransactionView(request):
    """
    ویوی مدیریت و پردازش فرم ثبت تراکنش جدید طلا توسط ادمین سیستم.
    """
    # در صورتی که نیاز به محدودسازی دسترسی ادمین باشد، می‌توان دکوراتور یا شرط نقش را اعمال کرد
    if not request.user.is_authenticated or request.user.role != 'admin':
        messages.error(request, "شما دسترسی لازم برای ورود به این بخش را ندارید.")
        return redirect('home') # یا هر مسیر پیش‌فرضی که دارید

    if request.method == 'POST':
        form = forms.GoldTransactionForm(request.POST)
        if form.is_valid():
            # استخراج داده‌های معتبر سازی شده از فرم
            cleaned_data = form.cleaned_data
            
            try:
                # فراخوانی لایه سرویس برای ثبت قطعی و اتمیک تراکنش در دیتابیس
                services.CreateGoldTransactionService(
                    customer_id=cleaned_data['customer'].id,
                    transaction_type=cleaned_data['transaction_type'],
                    gold_weight=cleaned_data['gold_weight'],
                    gold_price_per_gram=cleaned_data['gold_price_per_gram'],
                    recorded_by_id=request.user.id, # شناسه ادمین ثبت‌کننده
                    description=cleaned_data['description']
                )
                
                messages.success(request, "تراکنش طلا با موفقیت در سامانه ثبت شد.")
                return redirect('admin_panel:transactions_history') # فرض بر وجود لیست تراکنش‌ها
                
            except ValidationError as e:
                # مدیریت خطاهای بیزینس‌لاگیک (مانند عدم موجودی کافی برای برداشت)
                form.add_error(None, e.message)
    else:
        form = forms.GoldTransactionForm()

    context = {
        'form': form,
        'title': 'ثبت تراکنش جدید طلا'
    }
    
    # ارجاع به تمپلیت اختصاصی اپلیکیشن با الگوی Namespace
    return render(request, 'admin_panel/admin_transactions/admin_create_transactions.html', context)