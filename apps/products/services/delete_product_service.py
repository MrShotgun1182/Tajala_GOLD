from products import models

def DeleteProductService(product_id: int) -> bool:
    """
    حذف محصول از دیتابیس (تصاویر گالری به صورت Cascade خودکار حذف می‌شوند)
    """
    try:
        product = models.ProductModel.objects.get(id=product_id)
        product.delete()
        return True
    except models.ProductModel.DoesNotExist:
        return False