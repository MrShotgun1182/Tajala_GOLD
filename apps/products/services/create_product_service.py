from products import models
from decimal import Decimal

def CreateProductService(category_id: int,
title: str,
slug: str,
weight: Decimal,
image,
description: str = None,
gallery_images: list = None) -> models.ProductModel:
    """
    تابع خالص برای ایجاد محصول جدید همراه با مدیریت گالری تصاویر فرعی
    """
    product = models.ProductModel.objects.create(
        category_id=category_id,
        title=title,
        slug=slug,
        weight=weight,
        image=image,
        description=description
    )
    
    # اگر تصاویر فرعی برای گالری فرستاده شده بود
    if gallery_images:
        for img in gallery_images:
            models.ProductImageModel.objects.create(product=product, image=img)
            
    return product