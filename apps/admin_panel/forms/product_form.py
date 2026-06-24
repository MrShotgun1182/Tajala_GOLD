from django import forms
from django.core.exceptions import ValidationError
from products.models import ProductModel, ProductImageModel

class ProductForm(forms.ModelForm):
    class Meta:
        model = ProductModel
        fields = [
            'category',
            'title',
            'slug',
            'weight',
            'description',
            'image',
            'is_active'
        ]

    def clean_weight(self):
        """
        اعتبارسنجی اختصاصی وزن طلا جهت جلوگیری از وارد شدن وزن صفر یا منفی
        """
        weight = self.cleaned_data.get('weight')
        if weight is not None and weight <= 0:
            raise ValidationError("وزن طلا باید عددی مثبت و بزرگتر از صفر باشد.")
        return weight


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImageModel
        fields = ['image']