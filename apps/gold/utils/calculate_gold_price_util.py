from decimal import Decimal, ROUND_HALF_UP
from gold import utils

def CalculateGoldPriceUtil(
    gold_price_per_gram,
    weight,
    wage_percent=0,
    profit_percent=0,
    other_costs=0,
    tax_percent=0
) -> dict:
    # ۱. پاک‌سازی و تبدیل مطمئن ورودی‌ها
    price_per_gram = utils.clean_decimal_input(gold_price_per_gram)
    weight = utils.clean_decimal_input(weight)
    wage_pct = utils.clean_decimal_input(wage_percent)
    profit_pct = utils.clean_decimal_input(profit_percent)
    costs = utils.clean_decimal_input(other_costs)
    tax_pct = utils.clean_decimal_input(tax_percent)

    # ۲. محاسبه قیمت طلای خام
    raw_gold_price = weight * price_per_gram

    # ۳. محاسبه اجرت (بر اساس درصد از طلا خام)
    wage_amount = raw_gold_price * wage_pct / Decimal('100')

    # ۴. محاسبه سود فروشنده (بر اساس درصد از [طلا خام + اجرت])
    profit_base = raw_gold_price + wage_amount
    profit_amount = profit_base * profit_pct / Decimal('100')

    # ۵. محاسبه مالیات بر ارزش افزوده (طبق قانون: درصد از [اجرت + سود])
    tax_base = wage_amount + profit_amount
    tax_amount = tax_base * tax_pct / Decimal('100')

    # ۶. مجموع کل فاکتور
    total_price = raw_gold_price + wage_amount + profit_amount + costs + tax_amount

    # گرد کردن نهایی همگی به عدد صحیح (ریال)
    return {
        'raw_gold_price': raw_gold_price.quantize(Decimal('1'), rounding=ROUND_HALF_UP),
        'wage_amount': wage_amount.quantize(Decimal('1'), rounding=ROUND_HALF_UP),
        'profit_amount': profit_amount.quantize(Decimal('1'), rounding=ROUND_HALF_UP),
        'tax_amount': tax_amount.quantize(Decimal('1'), rounding=ROUND_HALF_UP),
        'other_costs': costs.quantize(Decimal('1'), rounding=ROUND_HALF_UP),
        'total_price': total_price.quantize(Decimal('1'), rounding=ROUND_HALF_UP)
    }