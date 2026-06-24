from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth import get_user_model

User = get_user_model()

class RegisterForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام',
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-gold-500'
        }),
        label="نام"
    )
    last_name = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            'placeholder': 'نام خانوادگی',
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-gold-500'
        }),
        label="نام خانوادگی"
    )
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
    confirm_password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'placeholder': 'تکرار رمز عبور',
            'class': 'w-full px-4 py-2 border rounded-lg focus:outline-none focus:ring-2 focus:ring-gold-500'
        }),
        label="تکرار رمز عبور"
    )

    def clean_phone_number(self):
        """
        اعتبارسنجی فرمت ایران و بررسی تکراری نبودن شماره تماس در سامانه تجلا
        """
        phone_number = self.cleaned_data.get('phone_number', '').strip()
        
        if not phone_number.isdigit():
            raise ValidationError("شماره تماس باید فقط شامل اعداد باشد.")
        if not phone_number.startswith('09'):
            raise ValidationError("شماره تماس باید با 09 شروع شود.")
            
        # بررسی یکتا بودن شماره در دیتابیس
        if User.objects.filter(phone_number=phone_number).exists():
            raise ValidationError("این شماره تماس قبلاً در سامانه ثبت شده است.")
            
        return phone_number

    def clean(self):
        """
        بررسی مطابقت رمز عبور و تکرار آن
        """
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise ValidationError("رمز عبور و تکرار آن با هم مطابقت ندارند.")
            
        return cleaned_data