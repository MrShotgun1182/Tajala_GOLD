from django.shortcuts import render
from categorys.models import ProductCategoryModel
from customers import services

def CustomerShowcaseView(request):
    """
    ویو رندر کاتالوگ و ویترین زیورآلات بر اساس استانداردهای تفکیک لایه‌ها
    """
    selected_category = request.GET.get('category', 'all')
    
    # فراخوانی لایه سرویس برای دریافت محصولات فعال
    products = services.GetActiveProductsService(category_slug=selected_category)
    
    # دریافت تمام دسته‌بندی‌ها برای داینامیک کردن دکمه‌های فیلتر بالایی
    categories = ProductCategoryModel.objects.all()
    
    context = {
        'products': products,
        'categories': categories,
        'current_category': selected_category
    }
    
    return render(request, 'customers/customer_product/customer_showcase.html', context)