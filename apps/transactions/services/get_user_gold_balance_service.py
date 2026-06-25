from decimal import Decimal
from transactions import models
from customers.models import CustomerModel

def GetUserGoldBalanceService(customer_id: int) -> Decimal:
    """
    محاسبه موجودی کل طلای یک مشتری بر اساس تراکنش‌های فعال و حذف‌نشده (deleted_at IS NULL).
    """
    try:
        # بررسی وجود مشتری در سامانه
        customer = CustomerModel.objects.get(id=customer_id)
    except CustomerModel.DoesNotExist:
        return Decimal('0.0000')

    # دریافت تمام تراکنش‌های فعال مشتری بر اساس کلید خارجی مدل جدید (customer_id)
    active_transactions = models.GoldTransactionModel.objects.filter(
        customer_id=customer.id,
        deleted_at__isnull=True
    )
    
    total_balance = Decimal('0.0000')
    
    for tx in active_transactions:
        if tx.transaction_type == 'DEPOSIT':
            total_balance += tx.gold_weight
        elif tx.transaction_type == 'WITHDRAWAL':
            total_balance -= tx.gold_weight
            
    return total_balance