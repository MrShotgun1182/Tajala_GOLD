from django import template

register = template.Library()

@register.filter(name='three_digits')
def three_digits(value):
    """
    جدا کردن سه رقمی اعداد (بدون تغییر زبان اعداد)
    """
    if value is None:
        return ""
    try:
        return f"{int(value):,}"
    except (ValueError, TypeError):
        return value

@register.filter(name='to_persian')
def to_persian(value):
    """
    تبدیل اعداد انگلیسی به فارسی
    """
    if value is None:
        return ""
    value_str = str(value)
    english_digits = "0123456789"
    persian_digits = "۰۱۲۳۴۵۶۷۸۹"
    translation_table = str.maketrans(english_digits, persian_digits)
    return value_str.translate(translation_table)