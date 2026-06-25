from django import forms
from django.core.exceptions import ValidationError
from decimal import Decimal
from transactions.models.gold_transaction_model import GoldTransactionModel

class GoldTransactionForm(forms.ModelForm):
    # فیلد کمکی برای تایپ شماره تلفن توسط ادمین
    customer_phone = forms.CharField(
        max_length=11,
        label="شماره تماس مشتری",
        widget=forms.TextInput(attrs={'placeholder': 'مثال: 09123456789'})
    )

    class Meta:
        model = GoldTransactionModel
        fields = [
            'customer', # این فیلد اصلی است که شناسه عددی را نگه می‌دارد
            'transaction_type',
            'gold_weight',
            'gold_price_per_gram',
            'description'
        ]
        widgets = {
            # تبدیل فیلد به هیدن چون جاوااسکریپت مقدار ID را در آن تزریق می‌کند
            'customer': forms.HiddenInput(), 
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # دیگر نیازی به Queryset سنگین در این بخش نیست!