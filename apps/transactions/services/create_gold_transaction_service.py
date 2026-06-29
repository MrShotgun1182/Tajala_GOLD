from decimal import Decimal
from django.db import transaction
from django.core.exceptions import ValidationError
from transactions.models.gold_transaction_model import GoldTransactionModel
from customers.models import CustomerModel
from transactions import services

def CreateGoldTransactionService(
    customer_id: int,
    transaction_type: str,
    gold_weight: Decimal,
    gold_price_per_gram: Decimal,
    recorded_by_id: int,
    description: str = None
) -> GoldTransactionModel:
    """
    سرویس ثبت تراکنش جدید طلا همراه با کنترل موجودی برای برداشت‌ها.
    """
    with transaction.atomic():
        # ۱. بررسی وجود مشتری
        try:
            customer = CustomerModel.objects.get(pk=customer_id)
        except CustomerModel.DoesNotExist:
            raise ValidationError("مشتری مورد نظر یافت نشد.")
            
        # ۲. بررسی کنترل موجودی در صورت برداشت
        if transaction_type == 'WITHDRAWAL':
            # از آنجا که بالانس بر اساس user_id محاسبه می‌شود، شناسه کاربر متصل به مشتری را می‌فرستیم
            current_balance = services.GetUserGoldBalanceService(customer.user_id)
            if current_balance < gold_weight:
                raise ValidationError(
                    f"موجود‌ی ناکافی است. موجودی فعلی: {current_balance} گرم، "
                    f"وزن درخواستی: {gold_weight} گرم."
                )
                
        # ۳. ثبت و ذخیره تراکنش در دیتابیس (اصلاح نام فیلد به customer)
        new_transaction = GoldTransactionModel.objects.create(
            customer=customer,
            transaction_type=transaction_type,
            gold_weight=gold_weight,
            gold_price_per_gram=gold_price_per_gram,
            recorded_by_id=recorded_by_id,
            description=description
        )
        
        return new_transaction