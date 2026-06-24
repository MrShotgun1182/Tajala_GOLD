from django.db import models
from products import models as products_image

class ProductImageModel(models.Model):
    """
    مدل تصاویر فرعی و گالری برای هر محصول
    """
    product = models.ForeignKey(
        products_image.ProductModel,
        on_delete=models.CASCADE,
        related_name='images', # با این نام می‌توانیم در تمپلیت به تصاویر دسترسی داشته باشیم (product.images.all)
        verbose_name="محصول مربوطه"
    )
    image = models.ImageField(upload_to='products/gallery/', verbose_name="تصویر گالری")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ بارگذاری")

    class Meta:
        verbose_name = "تصویر گالری محصول"
        verbose_name_plural = "گالری تصاویر محصولات"

    def __str__(self):
        return f"تصویر فرعی برای {self.product.title}"