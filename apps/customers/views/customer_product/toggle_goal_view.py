from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from customers import services

@login_required
@require_POST
def ToggleGoalView(request, slug):
    """
    ویو ایجکس (AJAX) برای نشان کردن یا حذف محصول از اهداف
    """
    is_added = services.ToggleCustomerGoalService(customer_user=request.user, product_slug=slug)
    
    return JsonResponse({
        'status': 'success',
        'is_added': is_added,
        'message': 'لیست اهداف بروزرسانی شد.'
    })