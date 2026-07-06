from celery import shared_task
# ایمپورت کردن مستقیم خود تابع سرویس
from apps.gold.services.fetch_and_store_gold_price_service import FetchAndStoreGoldPriceService

@shared_task(name='apps.gold.tasks.get_gold_price_task.GetGoldPriceTask')
def GetGoldPriceTask():
    print("[CELERY] Starting gold price fetch task...")
    
    try:
        # چون سرویس شما یک تابع است، اینجا مستقیماً آن را صدا می‌زنیم و اجرا می‌شود
        result = FetchAndStoreGoldPriceService()
        print(f"[CELERY] Function executed. Result status: {result}")
    except Exception as e:
        print(f"[CELERY] [ERROR] Something went wrong: {e}")
        
    return True