from decimal import Decimal
from django.db import transaction
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model
from transactions import services
from transactions import models

User = get_user_model()


def CreateGoldTransactionService(
    user_id: int,
    transaction_type: str,
    gold_weight: Decimal,
    gold_price_per_gram: Decimal,
    recorded_by_id: int,
    description: str = None
) -> models.GoldTransactionModel:
    """
    سرویس ثبت تراکنش جدید طلا همراه با کنترل موجودی برای برداشت‌ها.
    استفاده از atomic برای امنیت و یکپارچگی دیتابیس در صورت بروز خطا.
    """
    
    # استفاده از ساختار اتمیک جنگو برای قفل کردن عملیات در سطح دیتابیس
    with transaction.atomic():
        
        # ۱. بررسی وجود و صحت نقش کاربر (مشتری)
        try:
            customer = User.objects.get(pk=user_id, role='customer')
        except User.DoesNotExist:
            raise ValidationError("مشتری مورد نظر یافت نشد یا نقش او صحیح نیست.")
            
        # ۲. بررسی کنترل موجودی در صورت برداشت
        if transaction_type == 'WITHDRAWAL':
            current_balance = services.GetUserGoldBalance(user_id)
            if current_balance < gold_weight:
                raise ValidationError(
                    f"موجود‌ی ناکافی است. موجودی فعلی: {current_balance} گرم، "
                    f"وزن درخواستی: {gold_weight} گرم."
                )
                
        # ۳. ثبت و ذخیره تراکنش در دیتابیس
        new_transaction = models.GoldTransactionModel.objects.create(
            user=customer,
            transaction_type=transaction_type,
            gold_weight=gold_weight,
            gold_price_per_gram=gold_price_per_gram,
            recorded_by_id=recorded_by_id,
            description=description
        )
        
        return new_transaction