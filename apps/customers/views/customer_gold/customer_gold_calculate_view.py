from django.shortcuts import render
from gold import forms, utils

def CustomerGoldCalculateView(request):
    """
    ویوی محاسبه قیمت طلا برای پنل مدیریت بدون مقدار پیش‌فرض قیمت طلا
    """
    calculation_result = None

    if request.method == 'POST':
        form = forms.GoldCalculateForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            calculation_result = utils.CalculateGoldPriceUtil(
                gold_price_per_gram=data['gold_price_per_gram'],
                weight=data['weight'],
                wage_percent=data['wage_percent'],
                profit_percent=data['profit_percent'],
                other_costs=data['other_costs'],
                tax_percent=data['tax_percent']
            )
    else:
        form = forms.GoldCalculateForm()

    context = {
        'form': form,
        'result': calculation_result,
    }

    return render(request, 'customers/customer_gold/customer_gold_calculate.html', context)