import requests
from django.db import transaction
from gold import models  # اصلاح ایمپورت برای جلوگیری از تداخل مدل‌های جنگو و سلری

def FetchAndStoreGoldPriceService() -> bool:
    """
    این تابع به API متصل شده، لیست قیمت‌ها را گرفته، قیمت طلای ۱۸ عیار 
    را پیدا کرده و آن را در دیتابیس ثبت می‌کند.
    """
    print("[SERVICE] Executing function to fetch real gold price...")
    url = "https://Api.BrsApi.ir/Market/Gold_Currency.php?key=BIie41Y8ZjUpANHUDWWtKcMj9U6NAzP1" 
    
    # اضافه کردن هدر مرورگر واقعی برای عبور از فایروال ضد رباتِ سایت
    headers = {
        "Accept": "application/json",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
    }

    try:
        # فرستادن درخواست همراه با هدر و دور زدن اختلالات SSL داکر با verify=False
        response = requests.get(url, headers=headers, timeout=10, verify=False)
        
        if response.status_code == 200:
            data = response.json()
            gold_list = data.get("gold", [])
            
            gold_18k_data = None
            for item in gold_list:
                if item.get("symbol") == "IR_GOLD_18K":
                    gold_18k_data = item
                    break
            
            if gold_18k_data:
                current_price = gold_18k_data.get("price")
                
                if current_price is not None:
                    # استفاده از transaction.atomic برای ثبت آنی و قطعی در دیتابیس پستگرس داکر
                    with transaction.atomic():
                        models.GoldPrice.objects.create(price=current_price)
                    print(f"[SUCCESS] 18K Gold price updated in DB: {current_price}")
                    return True
            else:
                print("[ERROR] Symbol 'IR_GOLD_18K' not found in API response.")
                
        else:
            print(f"[ERROR] API returned status code: {response.status_code}")
            
    except requests.RequestException as e:
        print(f"[NETWORK ERROR] Failed to connect to Gold API: {e}")
        
    return False