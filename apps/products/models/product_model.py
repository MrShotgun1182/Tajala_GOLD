from django.db import models
from categorys.models import ProductCategoryModel

class ProductModel(models.Model):
    """
    مدل محصولات بخش ویترین (کاتالوگ زیورآلات تجلا)
    """
    category = models.ForeignKey(
        ProductCategoryModel,
        on_delete=models.CASCADE,
        related_name='products',
        verbose_name="دسته‌بندی"
    )
    title = models.CharField(max_length=200, verbose_name="نام محصول/زیورآلات")
    slug = models.SlugField(max_length=250, unique=True, allow_unicode=True, verbose_name="اسلاگ (URL)")
    
    # وزن طلا فیلد بسیار حیاتی برای محاسبه ارزش روز است
    weight = models.DecimalField(max_digits=6, decimal_places=3, verbose_name="وزن (گرم)")
    
    description = models.TextField(blank=True, null=True, verbose_name="توضیحات محصول")
    image = models.ImageField(upload_to='products/', verbose_name="تصویر اصلی محصول")
    
    # ========== فیلدهای جدید برای محاسبه قیمت ==========
    profit_percent = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0.00, 
        verbose_name="سود (%)"
    )
    
    wage_percent = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0.00, 
        verbose_name="اجرت (%)"
    )
    
    other_costs = models.DecimalField(
        max_digits=15, 
        decimal_places=0, 
        default=0, 
        verbose_name="هزینه‌های جانبی (ریال)"
    )
    
    tax_percent = models.DecimalField(
        max_digits=5, 
        decimal_places=2, 
        default=0.00, 
        verbose_name="مالیات (%)"
    )
    # ==================================================
    
    is_active = models.BooleanField(default=True, verbose_name="نمایش در ویترین")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        verbose_name = "محصول ویترین"
        verbose_name_plural = "محصولات ویترین"

    def __str__(self):
        return f"{self.title} ({self.weight} گرم)"