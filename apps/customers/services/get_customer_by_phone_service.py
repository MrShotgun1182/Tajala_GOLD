from django.core.exceptions import ValidationError
from customers.models import CustomerModel

def GetCustomerByPhoneService(phone_number: str) -> CustomerModel:
    """
    سرویس اختصاصی برای پیدا کردن مشتری بر اساس شماره تماس دقیق.
    در صورت عدم وجود، یک خطای معتبرسازی (ValidationError) پرتاب می‌کند.
    """
    if not phone_number:
        raise ValidationError("شماره تماس وارد نشده است.")

    try:
        # لود بهینه اطلاعات مشتری همراه با مدل کاربر متصل به آن
        customer = CustomerModel.objects.select_related('user').get(
            user__phone_number=phone_number
        )
        return customer
    except CustomerModel.DoesNotExist:
        raise ValidationError("مشتری با این شماره تماس در سامانه یافت نشد.")