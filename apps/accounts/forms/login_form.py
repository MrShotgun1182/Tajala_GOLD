from django import forms
from django.core.exceptions import ValidationError

class LoginForm(forms.Form):
    phone_number = forms.CharField(
        max_length=11,
        min_length=11,
        widget=forms.TextInput(attrs={
            'placeholder': 'شماره تماس (مثال: 09123456789)',
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-gold-500'
        }),
        label="شماره تماس"
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'رمز عبور',
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-gold-500'
        }),
        label="رمز عبور"
    )

    def clean_phone_number(self):
        """
        اعتبارسنجی اختصاصی برای فرمت شماره تلفن ایران
        """
        phone_number = self.cleaned_data.get('phone_number', '').strip()
        if not phone_number.isdigit():
            raise ValidationError("شماره تماس باید فقط شامل اعداد باشد.")
        if not phone_number.startswith('09'):
            raise ValidationError("شماره تماس باید با 09 شروع شود.")
        return phone_number