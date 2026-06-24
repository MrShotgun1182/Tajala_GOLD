from django.contrib import admin
from categorys.models import ProductCategoryModel

@admin.register(ProductCategoryModel)
class ProductCategoryModelAdmin(admin.ModelAdmin):
    # فیلدهایی که در لیست اصلی ادمین نمایش داده می‌شوند
    list_display = ('title', 'slug', 'created_at')
    
    # فیلدهایی که مدیر می‌تواند از طریق آن‌ها جستجو کند
    search_fields = ('title', 'slug')
    
    # فیلترهای سمت راست برای گزارش‌گیری سریع‌تر
    list_filter = ('created_at',)
    
    # پر شدن خودکار فیلد اسلاگ هم‌زمان با تایپ عنوان دسته‌بندی
    prepopulated_fields = {'slug': ('title',)}
    
    # مرتب‌سازی پیش‌فرض بر اساس جدیدترین‌ها
    ordering = ('-created_at',)