from categorys.models import ProductCategoryModel
from django.shortcuts import get_object_or_view_404

def GetProductCategoriesService():
    """
    دریافت تمام دسته‌بندی‌های بخش ویترین به ترتیب جدیدترین‌ها
    """
    return ProductCategoryModel.objects.all().order_by('-created_at')