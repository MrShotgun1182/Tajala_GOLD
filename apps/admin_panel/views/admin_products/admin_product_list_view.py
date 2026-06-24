from django.shortcuts import render
from products import services as products_services
from categorys import services as categorys_services

def AdminProductListView(request):
    """
    ویوی رندر کردن کاتالوگ و لیست محصولات فعال ویترین
    """
    products = products_services.GetActiveProductsService()
    categories = categorys_services.GetProductCategoriesService()
    
    context = {
        'products': products,
        'categories': categories,
    }
    
    return render(request, 'admin_panel/admin_products/admin_products_list.html', context)