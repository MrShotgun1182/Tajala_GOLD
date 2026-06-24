from categorys.models import ProductCategoryModel

def DeleteProductCategoryService(category_id: int) -> bool:
    """
    حذف یک دسته‌بندی بر اساس آی‌دی
    """
    try:
        category = ProductCategoryModel.objects.get(id=category_id)
        category.delete()
        return True
    except ProductCategoryModel.DoesNotExist:
        return False