from django.db import transaction
from customers.models.customers_model import CustomerModel

def UpdateCustomerService(
    customer_id: int,
    first_name: str = None,
    last_name: str = None,
    national_code: str = None,
    account_number: str = None,
    card_number: str = None,
    national_card_image = None
) -> CustomerModel:
    """
    سرویس خالص لایه برای به‌روزرسانی اطلاعات پروفایل مشتری (تکمیل اطلاعات اختیاری یا ویرایش مشخصات).
    """
    with transaction.atomic():
        # ۱. پیدا کردن پروفایل مشتری از دیتابیس
        try:
            customer = CustomerModel.objects.get(id=customer_id)
        except CustomerModel.DoesNotExist:
            raise ValueError("مشتری مورد نظر یافت نشد.")

        # ۲. به‌روزرسانی فیلدها در صورت ارسال مقادیر جدید
        if first_name is not None:
            customer.first_name = first_name
            
        if last_name is not None:
            customer.last_name = last_name
            
        if national_code is not None:
            customer.national_code = national_code
            
        if account_number is not None:
            customer.account_number = account_number
            
        if card_number is not None:
            customer.card_number = card_number
            
        if national_card_image is not None:
            customer.national_card_image = national_card_image

        # ۳. ذخیره تغییرات در دیتابیس
        customer.save()
        
        return customer