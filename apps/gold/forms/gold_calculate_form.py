from django import forms
from decimal import Decimal

class GoldCalculateForm(forms.Form):
    gold_price_per_gram = forms.DecimalField(
        max_digits=15,
        decimal_places=2,
        min_value=Decimal('1.00'),
        label="قیمت هر گرم طلا (ریال)",
        widget=forms.NumberInput(attrs={
            'step': '100'
        })
    )
    weight = forms.DecimalField(
        max_digits=8,
        decimal_places=3,
        min_value=Decimal('0.001'),
        label="وزن طلا (گرم)",
        widget=forms.NumberInput(attrs={
            'step': '0.001'
        })
    )
    wage_percent = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        min_value=Decimal('0.00'),
        initial=Decimal('7.00'),
        label="درصد اجرت (%)",
        widget=forms.NumberInput(attrs={
            'step': '0.1'
        })
    )
    profit_percent = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        min_value=Decimal('0.00'),
        initial=Decimal('7.00'),
        label="درصد سود (%)",
        widget=forms.NumberInput(attrs={
            'step': '0.1'
        })
    )
    other_costs = forms.DecimalField(
        max_digits=15,
        decimal_places=0,
        min_value=Decimal('0'),
        initial=Decimal('0'),
        label="هزینه‌های جانبی (ریال)",
        widget=forms.NumberInput(attrs={
            'step': '1000'
        })
    )
    tax_percent = forms.DecimalField(
        max_digits=5,
        decimal_places=2,
        min_value=Decimal('0.00'),
        initial=Decimal('10.00'),
        label="درصد مالیات (%)",
        widget=forms.NumberInput(attrs={
            'step': '1'
        })
    )