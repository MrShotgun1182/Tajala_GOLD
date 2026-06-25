from products import models

def GetProductDetailService(slug: str) -> models.ProductModel:
    """
    سرویس خالص برای دریافت اطلاعات کامل یک محصول همراه با تصاویر گالری آن
    """
    try:
        # با prefetch_related تصاویر گالری فرعی را یک‌جا واکشی می‌کنیم تا کوئری اضافه نخورد
        return models.ProductModel.objects.filter(is_active=True).prefetch_related('images').get(slug=slug)
    except models.ProductModel.DoesNotExist:
        return None