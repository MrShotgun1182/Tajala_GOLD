# apps/products/views/add_product_view.py
from django.shortcuts import render, redirect
from django.contrib import messages
from admin_panel import forms
from products.services.create_product_service import CreateProductService

def AdminCreateProductView(request):
    """
    ویوی مدیریت جهت نمایش و پردازش فرم اضافه کردن محصول جدید به همراه گالری تصاویر
    """
    # TODO: در آینده با دکوراتور یا شرط، دسترسی را فقط به کاربرانی با نقش admin محدود می‌کنیم.
    
    if request.method == 'POST':
        form = forms.ProductForm(request.POST, request.FILES)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            
            # دریافت فایل‌های مربوط به گالری تصاویر فرعی از ریکوئست
            gallery_images = request.FILES.getlist('gallery_images')
            
            # فراخوانی سرویس اختصاصی با فیلدهای جدید محاسباتی
            product = CreateProductService(
                category_id=cleaned_data['category'].id if cleaned_data['category'] else None,
                title=cleaned_data['title'],
                slug=cleaned_data['slug'],
                weight=cleaned_data['weight'],
                profit_percent=cleaned_data['profit_percent'],
                wage_percent=cleaned_data['wage_percent'],
                other_costs=cleaned_data['other_costs'],
                tax_percent=cleaned_data['tax_percent'],
                image=cleaned_data['image'],
                description=cleaned_data['description'],
                is_active=cleaned_data['is_active'],
                gallery_images=gallery_images
            )
            
            messages.success(request, f"محصول «{product.title}» با موفقیت به کاتالوگ اضافه شد.")
            return redirect('admin_panel:create_product')
    else:
        form = forms.ProductForm()

    context = {
        'form': form,
        'title_page': 'افزودن محصول جدید به کاتالوگ'
    }
    return render(request, 'admin_panel/admin_products/admin_create_product.html', context)