from customers import models as customers_models
from products import models as products_models

def ToggleCustomerGoalService(customer_user, product_slug: str) -> bool:
    """
    سرویس افزودن یا حذف محصول از لیست اهداف مشتری.
    خروجی True یعنی محصول اضافه شد و False یعنی حذف شد.
    """
    try:
        customer = customers_models.CustomerModel.objects.get(user=customer_user)
        product = products_models.ProductModel.objects.get(slug=product_slug)
        
        goal_exists = customers_models.CustomerGoalModel.objects.filter(customer=customer, product=product).exists()
        
        if goal_exists:
            customers_models.CustomerGoalModel.objects.filter(customer=customer, product=product).delete()
            return False # حذف شد
        else:
            customers_models.CustomerGoalModel.objects.create(customer=customer, product=product)
            return True # اضافه شد
            
    except (customers_models.CustomerModel.DoesNotExist, products_models.ProductModel.DoesNotExist):
        return False