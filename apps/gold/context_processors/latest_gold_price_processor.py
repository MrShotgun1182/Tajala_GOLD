from gold.models import GoldPrice

def LatestGoldPrice(request):
    """
    تزریق سراسری آخرین قیمت طلا به تمام تمپلیت‌ها
    """
    try:
        latest_record = GoldPrice.objects.latest('created_at')
        price = latest_record.price
    except GoldPrice.DoesNotExist:
        price = 0

    return {
        'gold_price': price
    }