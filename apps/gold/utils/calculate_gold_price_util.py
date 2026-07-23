from decimal import Decimal, ROUND_HALF_UP

def CalculateGoldPriceUtil(
    gold_price_per_gram: Decimal,
    weight: Decimal,
    wage_percent: Decimal = Decimal('0.00'),
    profit_percent: Decimal = Decimal('0.00'),
    other_costs: Decimal = Decimal('0'),
    tax_percent: Decimal = Decimal('0.00')
) -> dict:
    """
    محاسبه قیمت نهایی طلا بر اساس ضوابط مالی و فرمول رسمی اتحادیه.
    تمام محاسبات با تایپ Decimal انجام می‌شود تا از خطاهای اعشاری float جلوگیری شود.
    """
    # تبدیل ورودی‌ها به Decimal در صورت ارسال فرمت‌های دیگر
    price_per_gram = Decimal(str(gold_price_per_gram))
    weight = Decimal(str(weight))
    wage_pct = Decimal(str(wage_percent))
    profit_pct = Decimal(str(profit_percent))
    costs = Decimal(str(other_costs))
    tax_pct = Decimal(str(tax_percent))

    # ۱. محاسبه قیمت طلای خام
    raw_gold_price = weight * price_per_gram

    # ۲. محاسبه اجرت (درصد از قیمت طلای خام)
    wage_amount = raw_gold_price * (wage_pct / Decimal('100'))

    # ۳. محاسبه سود فروشنده (درصد از مجموع طلا + اجرت)
    profit_amount = (raw_gold_price + wage_amount) * (profit_pct / Decimal('100'))

    # ۴. محاسبه مالیات بر ارزش افزوده (درصد از سود + اجرت)
    tax_amount = (wage_amount + profit_amount) * (tax_pct / Decimal('100'))

    # ۵. قیمت کل نهایی
    total_price = raw_gold_price + wage_amount + profit_amount + costs + tax_amount

    # گرد کردن قیمت نهایی به عدد صحیح (ریال)
    total_price_rounded = total_price.quantize(Decimal('1'), rounding=ROUND_HALF_UP)

    return {
        'raw_gold_price': raw_gold_price.quantize(Decimal('1')),
        'wage_amount': wage_amount.quantize(Decimal('1')),
        'profit_amount': profit_amount.quantize(Decimal('1')),
        'tax_amount': tax_amount.quantize(Decimal('1')),
        'other_costs': costs,
        'total_price': total_price_rounded
    }