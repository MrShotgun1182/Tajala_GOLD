from decimal import Decimal

def clean_decimal_input(val) -> Decimal:
    """
    پاک‌سازی کامل ورودی‌های عددی و اعشاری از کیبوردهای فارسی/عربی و کاراکترهای جداکننده
    """
    if val is None or val == '':
        return Decimal('0')
    
    # اگر ورودی از قبل Decimal یا int/float باشد
    if isinstance(val, (int, float, Decimal)):
        return Decimal(str(val))
    
    s = str(val).strip()
    
    # ۱. تبدیل اعداد فارسی و عربی به انگلیسی
    persian_digits = '۰۱۲۳۴۵۶۷۸۹'
    arabic_digits = '٠١٢٣٤٥٦٧٨٩'
    for i in range(10):
        s = s.replace(persian_digits[i], str(i)).replace(arabic_digits[i], str(i))
    
    # ۲. حذف کاما و فاصله‌های اضافه
    s = s.replace(',', '').replace(' ', '')
    
    # ۳. تبدیل ممیز فارسی (٫) به نقطه انگلیسی (.)
    s = s.replace('٫', '.')
    
    # ۴. اگر بیش از یک نقطه وجود داشت (مثلاً جداکننده هزارگان غلط)، فقط آخرین نقطه مربوط به اعشار است
    if s.count('.') > 1:
        parts = s.split('.')
        s = "".join(parts[:-1]) + "." + parts[-1]
        
    try:
        return Decimal(s)
    except Exception:
        return Decimal('0')