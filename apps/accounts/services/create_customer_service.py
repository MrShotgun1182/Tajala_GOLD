from django.db import transaction
from django.contrib.auth import get_user_model
from customers.models.customers_model import CustomerModel

User = get_user_model()

def CreateCustomerService(
    phone_number: str,
    password: str,
    first_name: str,
    last_name: str
) -> CustomerModel:
    """
    سرویس خالص ثبت‌نام اولیه مشتری؛ فقط با فیلدهای ۱۰۰٪ اجباری.
    """
    with transaction.atomic():
        
        # ۱. ایجاد کاربر پایه در UserModel با نقش مشتری
        user = User.objects.create_user(
            username=phone_number,
            phone_number=phone_number,
            password=password,
            role='customer'
        )
        
        # ۲. ایجاد پروفایل اولیه در CustomerModel و اتصال به کاربر
        customer = CustomerModel.objects.create(
            user=user,
            first_name=first_name,
            last_name=last_name
        )
        
        return customer