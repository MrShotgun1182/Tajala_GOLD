from django import forms
from django.core.exceptions import ValidationError
from decimal import Decimal
from transactions.models.gold_transaction_model import GoldTransactionModel
from customers.models import CustomerModel

class GoldTransactionForm(forms.ModelForm):
    class Meta:
        model = GoldTransactionModel
        fields = [
            'customer',
            'transaction_type',
            'gold_weight',
            'gold_price_per_gram',
            'description'
        ]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # بهینه‌سازی کوئری دیتابیس برای لود اطلاعات متصل به کاربر
        self.fields['customer'].queryset = CustomerModel.objects.select_related('user').all()

    def clean_gold_weight(self):
        """
        اعتبارسنجی اختصاصی وزن طلا جهت جلوگیری از وارد شدن مقدار صفر یا منفی
        """
        gold_weight = self.cleaned_data.get('gold_weight')
        if gold_weight is not None and gold_weight <= Decimal('0.0000'):
            raise ValidationError("وزن طلا باید عددی مثبت و بزرگتر از صفر باشد.")
        return gold_weight

    def clean_gold_price_per_gram(self):
        """
        اعتبارسنجی اختصاصی قیمت هر گرم طلا جهت جلوگیری از مقادیر نامعتبر مالی
        """
        gold_price = self.cleaned_data.get('gold_price_per_gram')
        if gold_price is not None and gold_price <= 0:
            raise ValidationError("قیمت هر گرم طلا باید عددی مثبت و بزرگتر از صفر باشد.")
        return gold_price