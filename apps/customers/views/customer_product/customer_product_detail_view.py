from django.shortcuts import render, get_object_or_404
from django.http import Http404
from products.services.get_product_detail_service import GetProductDetailService

def ProductDetailView(request, slug):
    """
    ویو مدیریت درخواست نمایش جزئیات محصول و رندر تمپلیت
    """
    product = GetProductDetailService(slug=slug)
    
    if not product:
        raise Http404("محصول مورد نظر یافت نشد 😐")
        
    context = {
        'product': product
    }
    
    return render(request, 'customers/customer_product/customer_product_detail.html', context)