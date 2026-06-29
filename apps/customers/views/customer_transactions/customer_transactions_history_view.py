from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from customers import services

@login_required
def CustomerTransactionsHistoryView(request):
    """
    ویوی لایه نمایش تاریخچه تراکنش‌ها برای مشتری متصل شده به سیستم
    """
    # دریافت پروفایل مشتری از کاربر لاگین شده
    customer = request.user.customer_profile
    
    # فراخوانی سرویس برای دریافت تراکنش‌های معتبر بر اساس مدل شما
    transactions = services.GetCustomerTransactionsService(customer.id)
    
    context = {
        'customer': customer,
        'transactions': transactions,
    }
    
    return render(request, 'customers/customer_transactions/customer_transactions_history.html', context)