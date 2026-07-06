import os
from celery import Celery
from celery.schedules import crontab

# معرفی فایل تنظیمات جنگو به سلری
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')

app = Celery('core')

# خواندن تنظیمات سلری از داخل settings.py با پیشوند CELERY_
app.config_from_object('django.conf:settings', namespace='CELERY')

# جستجوی خودکار در تمام اپ‌ها برای پیدا کردن تسک‌ها (فایل‌های tasks.py)
app.autodiscover_tasks()

# برنامه زمان‌بندی: تعریف کارِ تکرار شونده (هر ۱ دقیقه)
app.conf.beat_schedule = {
    'fetch-gold-price-every-minute': {
        'task': 'apps.gold.tasks.get_gold_price_task.GetGoldPriceTask', # آدرس و نام دقیق با کمل‌کیس
        'schedule': crontab(minute='*'), # هر دقیقه
    },
}