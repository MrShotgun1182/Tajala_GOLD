from django.db import models

class ProductCategoryModel(models.Model):
    """
    مدل دسته‌بندی محصولات بخش ویترین (کاتالوگ زیورآلات تجلا)
    """
    title = models.CharField(max_length=100, verbose_name="عنوان دسته‌بندی ویترین")
    slug = models.SlugField(max_length=120, unique=True, allow_unicode=True, verbose_name="اسلاگ (URL)")
    image = models.ImageField(upload_to='categories/products/', blank=True, null=True, verbose_name="تصویر آیکون/دسته‌بندی")
    
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ایجاد")

    class Meta:
        verbose_name = "دسته‌بندی محصول ویترین"
        verbose_name_plural = "دسته‌بندی‌های محصولات ویترین"

    def __str__(self):
        return self.title