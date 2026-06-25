from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ValidationError
from customers.services.get_customer_by_phone_service import GetCustomerByPhoneService

@login_required
def AdminCustomerSearchApi(request):
    """
    API ادمین برای استعلام آنی اطلاعات مشتری با ارسال شماره تماس.
    تمام منطق دیتابیس به لایه سرویس منتقل شده است.
    """
    phone_number = request.GET.get('phone_number', '').strip()
    
    try:
        # فراخوانی سرویس برای دریافت اطلاعات مشتری
        customer = GetCustomerByPhoneService(phone_number=phone_number)
        
        return JsonResponse({
            'success': True,
            'customer_id': customer.id,
            'full_name': customer.full_name,
            'national_code': customer.national_code
        })
        
    except ValidationError as e:
        # مدیریت خطاهای پرتاب شده از لایه سرویس
        return JsonResponse({
            'success': False, 
            'error': e.message
        }, status=400)