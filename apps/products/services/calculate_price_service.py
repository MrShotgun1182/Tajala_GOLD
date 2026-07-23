def CalculatePriceService(self, gold_price_per_gram: float) -> dict:
    """
    محاسبه قیمت نهایی محصول بر اساس قیمت روز طلا
    
    پارامترها:
        gold_price_per_gram: قیمت هر گرم طلا به ریال
    
    بازگشت:
        دیکشنری شامل قیمت طلای خام، سود، اجرت، مالیات، هزینه‌های جانبی و قیمت نهایی
    """
    raw_gold_price = self.weight * gold_price_per_gram
    
    profit_amount = raw_gold_price * (self.profit_percent / 100)
    wage_amount = raw_gold_price * (self.wage_percent / 100)
    
    price_before_tax = raw_gold_price + profit_amount + wage_amount + self.other_costs
    
    tax_amount = price_before_tax * (self.tax_percent / 100)
    
    final_price = price_before_tax + tax_amount
    
    return {
        'raw_gold_price': raw_gold_price,          # قیمت طلای خام
        'profit_amount': profit_amount,            # مبلغ سود
        'wage_amount': wage_amount,                # مبلغ اجرت
        'other_costs': self.other_costs,           # هزینه‌های جانبی
        'tax_amount': tax_amount,                  # مبلغ مالیات
        'final_price': final_price                 # قیمت نهایی
    }