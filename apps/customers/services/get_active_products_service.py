from django.db.models import QuerySet
from products.models.product_model import ProductModel

def GetActiveProductsService(category_slug: str = None) -> QuerySet:
    """
    سرویس خالص برای دریافت لیست محصولات فعال ویترین به همراه فیلتر دسته‌بندی
    """
    # ابتدا فقط محصولاتی که وضعیت نمایش در ویترین آن‌ها فعال است را می‌گیریم
    queryset = ProductModel.objects.filter(is_active=True).select_related('category')
    
    # اعمال فیلتر بر اساس اسلاگ دسته‌بندی در صورت ارسال
    if category_slug and category_slug != 'all':
        queryset = queryset.filter(category__slug=category_slug)
        
    return queryset