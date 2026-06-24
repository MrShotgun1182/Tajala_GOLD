from decimal import Decimal
from django.contrib.auth import get_user_model
from transactions import models
from django.core.exceptions import ObjectDoesNotExist

User = get_user_model()

def GetUserGoldBalanceService(user_id: int) -> Decimal:
    """
    محاسبه موجودی کل طلای یک کاربر بر اساس تراکنش‌های فعال مشتری (حذف‌نشده).
    """
    try:
        # پیدا کردن کاربر و دریافت ایدی پروفایل مشتری او
        user = User.objects.get(id=user_id)
        # با توجه به related_name='customer_profile' در مدل مشتری شما:
        customer_id = user.customer_profile.id
    except (User.DoesNotExist, ObjectDoesNotExist):
        return Decimal('0.0000')

    # دریافت تمام تراکنش‌های حذف‌نشده با استفاده از کلید واژه درست دیتابیس (customer_id)
    active_transactions = models.GoldTransactionModel.objects.filter(
        customer_id=customer_id,
        deleted_at__isnull=True
    )
    
    total_balance = Decimal('0.0000')
    
    for tx in active_transactions:
        if tx.transaction_type == 'DEPOSIT':
            total_balance += tx.gold_weight
        elif tx.transaction_type == 'WITHDRAWAL':
            total_balance -= tx.gold_weight
            
    return total_balance