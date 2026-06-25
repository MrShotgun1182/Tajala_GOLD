from customers.models.customer_goal_model import CustomerGoalModel

def CheckProductTargetedService(user, product) -> bool:
    """
    بررسی اینکه آیا محصول توسط مشتری فعلی هدف قرار گرفته است یا خیر
    """
    if not user.is_authenticated or user.role != 'customer':
        return False
        
    return CustomerGoalModel.objects.filter(
        customer__user=user, 
        product=product
    ).exists()