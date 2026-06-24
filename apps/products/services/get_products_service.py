from products import models
from django.shortcuts import get_object_or_404

def GetActiveProductsService():
    """
    دریافت تمام محصولات فعال ویترین به همراه دسته‌بندی آن‌ها (استفاده از select_related برای بهینه‌سازی کوئری)
    """
    return models.ProductModel.objects.filter(is_active=True).select_related('category').order_by('-created_at')

def GetProductBySlugService(slug: str) -> models.ProductModel:
    """
    دریافت یک محصول خاص بر اساس اسلاگ برای صفحه جزئیات محصول
    """
    return get_object_or_404(models.ProductModel, slug=slug, is_active=True)