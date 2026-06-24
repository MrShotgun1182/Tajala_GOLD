from categorys.models import ProductCategoryModel

def UpdateProductCategoryService(category_id: int, title: str = None, slug: str = None, image=None) -> ProductCategoryModel:
    """
    بروزرسانی اطلاعات یک دسته‌بندی موجود
    """
    category = ProductCategoryModel.objects.get(id=category_id)
    
    if title:
        category.title = title
    if slug:
        category.slug = slug
    if image is not None:
        category.image = image
        
    category.save()
    return category