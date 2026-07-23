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
            'profit_percent',
            'wage_percent',
            'other_costs',
            'tax_percent',
            'description',
            'image',
            'is_active',
        ]

    def clean_weight(self):
        """
        اعتبارسنجی اختصاصی وزن طلا جهت جلوگیری از وارد شدن وزن صفر یا منفی
        """
        weight = self.cleaned_data.get('weight')
        if weight is not None and weight <= 0:
            raise ValidationError("وزن طلا باید عددی مثبت و بزرگتر از صفر باشد.")
        return weight

    def clean_profit_percent(self):
        """
        اعتبارسنجی درصد سود
        """
        profit_percent = self.cleaned_data.get('profit_percent')
        if profit_percent is not None and profit_percent < 0:
            raise ValidationError("درصد سود نمی‌تواند عددی منفی باشد.")
        return profit_percent

    def clean_wage_percent(self):
        """
        اعتبارسنجی درصد اجرت
        """
        wage_percent = self.cleaned_data.get('wage_percent')
        if wage_percent is not None and wage_percent < 0:
            raise ValidationError("درصد اجرت نمی‌تواند عددی منفی باشد.")
        return wage_percent

    def clean_other_costs(self):
        """
        اعتبارسنجی هزینه‌های جانبی (ریال)
        """
        other_costs = self.cleaned_data.get('other_costs')
        if other_costs is not None and other_costs < 0:
            raise ValidationError("هزینه‌های جانبی نمی‌تواند عددی منفی باشد.")
        return other_costs

    def clean_tax_percent(self):
        """
        اعتبارسنجی درصد مالیات
        """
        tax_percent = self.cleaned_data.get('tax_percent')
        if tax_percent is not None and tax_percent < 0:
            raise ValidationError("درصد مالیات نمی‌تواند عددی منفی باشد.")
        return tax_percent


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImageModel
        fields = ['image']