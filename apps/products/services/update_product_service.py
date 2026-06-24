from products import models
from decimal import Decimal

def UpdateProductService(
    product_id: int,
    category_id: int = None,
    title: str = None,
    slug: str = None,
    weight: Decimal = None,
    image = None,
    description: str = None,
    is_active: bool = None,
    new_gallery_images: list = None) -> models.ProductModel:
    """
    بروزرسانی اطلاعات محصول و افزودن تصاویر جدید به گالری
    """
    product = models.ProductModel.objects.get(id=product_id)
    
    if category_id:
        product.category_id = category_id
    if title:
        product.title = title
    if slug:
        product.slug = slug
    if weight is not None:
        product.weight = weight
    if image is not None:
        product.image = image
    if description is not None:
        product.description = description
    if is_active is not None:
        product.is_active = is_active
        
    product.save()
    
    # افزودن تصاویر جدید به گالری در صورت وجود
    if new_gallery_images:
        for img in new_gallery_images:
            models.ProductImageModel.objects.create(product=product, image=img)
            
    return product