from categorys.models import ProductCategoryModel

def CreateProductCategoryService(title: str, slug: str, image=None) -> ProductCategoryModel:
    """
    تابع خالص برای ایجاد یک دسته‌بندی جدید در ویترین محصولات
    """
    category = ProductCategoryModel.objects.create(
        title=title,
        slug=slug,
        image=image
    )
    return category