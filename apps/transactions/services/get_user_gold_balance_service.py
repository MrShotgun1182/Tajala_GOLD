from decimal import Decimal
from django.contrib.auth import get_user_model
from transactions import models

User = get_user_model()

def GetUserGoldBalanceService(user_id: int) -> Decimal:
    """
    محاسبه موجودی کل طلای یک کاربر بر اساس تراکنش‌های فعال (حذف‌نشده).
    """
    # دریافت تمام تراکنش‌های حذف‌نشده کاربر
    active_transactions = models.GoldTransactionModel.objects.filter(
        user_id=user_id,
        deleted_at__isnull=True
    )
    
    total_balance = Decimal('0.0000')
    
    for tx in active_transactions:
        if tx.transaction_type == 'DEPOSIT':
            total_balance += tx.gold_weight
        elif tx.transaction_type == 'WITHDRAWAL':
            total_balance -= tx.gold_weight
            
    return total_balance