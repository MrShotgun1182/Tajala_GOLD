from customers import models

def GetCustomerGoalsService(customer_user):
    """
    سرویس دریافت لیست اهداف خرید مشتری به همراه اطلاعات کامل محصول
    """
    if not customer_user.is_authenticated:
        return []
        
    return models.CustomerGoalModel.objects.filter(
        customer__user=customer_user
    ).select_related('product')