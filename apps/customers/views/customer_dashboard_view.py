from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from transactions import services as transactions_services

@login_required(login_url='accounts:login')
def CustomerDashboardView(request):
    user_id = request.user.id
    
    # ۱. فراخوانی لایه سرویس اختصاصی شما برای محاسبه موجودی دقیق طلا
    gold_balance = transactions_services.GetUserGoldBalanceService(user_id)
    gold_price_per_gram = 160000000  
    
    # ۳. محاسبه ارزش ریالی کل دارایی طلای مشتری
    total_currency_value = gold_balance * gold_price_per_gram
    
    context = {
        'gold_balance': gold_balance,
        'gold_price_per_gram': gold_price_per_gram,
        'total_currency_value': total_currency_value,
    }
    return render(request, 'customers/customer_dashboard.html', context=context)