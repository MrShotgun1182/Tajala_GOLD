from categorys.models import ProductCategoryModel

def GetProductCategoriesService():
    """
    دریافت تمام دسته‌بندی‌های بخش ویترین به ترتیب جدیدترین‌ها
    """
    return ProductCategoryModel.objects.all().order_by('-created_at')