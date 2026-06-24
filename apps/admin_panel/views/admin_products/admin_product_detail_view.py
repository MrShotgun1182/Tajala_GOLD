from django.shortcuts import render
from products import services as products_services

def AdminProductDetailView(request, slug):
    """
    ویوی نمایش جزئیات یک محصول خاص به همراه گالری تصاویر آن
    """
    product = products_services.GetProductBySlugService(slug=slug)
    
    context = {
        'product': product,
    }
    
    return render(request, 'admin_panel/admin_products/product_detail.html', context)