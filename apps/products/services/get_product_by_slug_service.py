from products import models
from django.shortcuts import get_object_or_404

def GetProductBySlugService(slug: str) -> models.ProductModel:
    """
    دریافت یک محصول خاص بر اساس اسلاگ برای صفحه جزئیات محصول
    """
    return get_object_or_404(models.ProductModel, slug=slug, is_active=True)