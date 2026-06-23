from django.contrib.auth.models import AbstractUser
from django.db import models

class UserModel(AbstractUser):
    ROLE_CHOICES = (
        ('admin', 'مدیر فروشگاه'),
        ('customer', 'مشتری'),
    )
    
    role = models.CharField(
        max_length=10, 
        choices=ROLE_CHOICES, 
        default='customer',
        verbose_name="نقش کاربری"
    )
    
    phone_number = models.CharField(
        max_length=11, 
        unique=True, 
        verbose_name="شماره تماس"
    )
    
    USERNAME_FIELD = 'phone_number'
    
    REQUIRED_FIELDS = ['username', 'email']
    
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"

    def __str__(self):
        full_name = self.get_full_name()
        return full_name if full_name else self.phone_number
    
    def save(self, *args, **kwargs):
        # اگر کاربر سوپریوزر یا کارمند (is_staff) بود، نقش او را به صورت خودکار ادمین قرار بده
        if self.is_superuser or self.is_staff:
            self.role = 'admin'
        super().save(*args, **kwargs)