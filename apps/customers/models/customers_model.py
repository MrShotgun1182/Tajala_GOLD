from django.db import models
from django.conf import settings

class CustomerModel(models.Model):
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='customer_profile',
        verbose_name="کاربر مربوطه"
    )
    
    first_name = models.CharField(max_length=100, verbose_name="نام")
    last_name = models.CharField(max_length=150, verbose_name="نام خانوادگی")
    
    national_code = models.CharField(
        max_length=10, 
        unique=True, 
        blank=True, # اضافه شد
        null=True,  # اضافه شد
        verbose_name="کد ملی"
    )
        
    account_number = models.CharField(
        max_length=30, 
        blank=True, 
        null=True, 
        verbose_name="شماره حساب بانکی"
    )
    
    card_number = models.CharField(
        max_length=16, 
        blank=True, 
        null=True, 
        verbose_name="شماره کارت بانکی"
    )
    
    # ذخیره عکس کارت ملی در یک پوشه مجزا
    national_card_image = models.ImageField(
        upload_to='customers/national_cards/',
        blank=True,
        null=True,
        verbose_name="تصویر کارت ملی"
    )
    
    # فیلدهای زمانی برای گزارش‌گیری و رهگیری
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ثبت نام")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="آخرین بروزرسانی")

    class Meta:
        verbose_name = "پروفایل مشتری"
        verbose_name_plural = "پروفایل‌های مشتریان"

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.user.phone_number})"
    
    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"