from django import template
from decimal import Decimal
from transactions.services import GetUserGoldBalanceService
from gold.services import GetLatestGoldPriceService

register = template.Library()

@register.simple_tag
def CustomerGoldBalanceTag(user) -> dict:
    """
    محاسبه و بازگرداندن موجودی طلا (به گرم) و ارزش ریالی آن به صورت دیکشنری.
    """
    # مقادیر پیش‌فرض برای کاربران احراز هویت نشده یا در صورت بروز خطا
    default_data = {
        'gold_balance': Decimal('0.000'),
        'rial_balance': Decimal('0.00')
    }

    if not user or not user.is_authenticated:
        return default_data

    try:
        customer = user.customer_profile
        
        # ۱. دریافت موجودی طلای کاربر به گرم (از سرویس شما)
        gold_balance = GetUserGoldBalanceService(customer.id)
        if not gold_balance:
            gold_balance = Decimal('0.000')

        # ۲. دریافت آخرین قیمت ثبت شده طلا (از سرویس جدید)
        latest_price = GetLatestGoldPriceService()
        if not latest_price:
            latest_price = Decimal('0.00')

        # ۳. محاسبه ارزش ریالی موجودی طلا
        rial_balance = gold_balance * latest_price

        return {
            'gold_balance': gold_balance,
            'rial_balance': rial_balance
        }

    except Exception:
        return default_data