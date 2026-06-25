from django.db.models import Q, QuerySet
from transactions import models

def FilterGoldTransactionsService(search_query: str = None, tx_type: str = None) -> QuerySet:
    """
    سرویس فیلتر و جستجوی تراکنش‌های طلا جهت نمایش در تاریخچه ادمین.
    تراکنش‌های حذف نرم شده (deleted_at) به طور خودکار فیلتر می‌شوند.
    """
    # قدم اول: دریافت تراکنش‌های زنده به همراه لود بهینه اطلاعات مشتری و کاربر متصل به آن
    queryset = models.GoldTransactionModel.objects.filter(
        deleted_at__isnull=True
    ).select_related('customer__user', 'recorded_by')
    
    # قدم دوم: اعمال فیلتر نوع تراکنش (DEPOSIT / WITHDRAWAL)
    if tx_type in ['DEPOSIT', 'WITHDRAWAL']:
        queryset = queryset.filter(transaction_type=tx_type)
        
    # قدم سوم: اعمال جستجوی متنی روی اطلاعات پروفایل مشتری و شماره تماس کاربر
    if search_query:
        search_query = search_query.strip()
        queryset = queryset.filter(
            Q(customer__first_name__icontains=search_query) |
            Q(customer__last_name__icontains=search_query) |
            Q(customer__user__phone_number__icontains=search_query)
        )
        
    return queryset