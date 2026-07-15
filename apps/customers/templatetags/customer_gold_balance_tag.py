# apps/customers/templatetags/customer_gold_balance_tag.py

from django import template
from decimal import Decimal
from transactions.services import GetUserGoldBalanceService

register = template.Library()

@register.simple_tag
def CustomerGoldBalanceTag(user) -> Decimal:
    """
    ساده‌ترین شکل ممکن تگ: فقط کاربر را می‌گیرد و موجودی او را برمی‌گرداند.
    """
    if not user or not user.is_authenticated:
        return Decimal('0.0000')

    try:
        # دسترسی به پروفایل مشتری[cite: 5]
        customer = user.customer_profile
        # فراخوانی مستقیم سرویس
        return GetUserGoldBalanceService(customer.id)
    except Exception:
        return Decimal('0.0000')