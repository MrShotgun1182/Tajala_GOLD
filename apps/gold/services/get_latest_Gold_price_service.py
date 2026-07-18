from decimal import Decimal
from typing import Optional
from gold import models

def GetLatestGoldPriceService() -> Optional[Decimal]:
    """
    سرویس دریافت آخرین قیمت ثبت شده طلا در سیستم
    """
    latest_record = models.GoldPrice.objects.first()
    
    if latest_record:
        return latest_record.price
        
    return None