from transactions import models

def GetCustomerTransactionsService(customer_id: int):
    """
    سرویس دریافت تراکنش‌های فعال یک مشتری (تراکنش‌های حذف نرم نشده)
    """
    transactions = models.GoldTransactionModel.objects.filter(
        customer_id=customer_id,
        deleted_at__isnull=True
    ).select_related('recorded_by') # بهینه‌سازی کوئری برای دریافت نام مدیر
    
    # اضافه کردن ارزش ریالی هر تراکنش به صورت پویا برای راحتی کار در تمپلیت
    for tx in transactions:
        tx.total_cal_price = tx.gold_weight * tx.gold_price_per_gram
        
    return transactions