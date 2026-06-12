from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import UserModel

@admin.register(UserModel)
class CustomUserAdmin(UserAdmin):
    # نمایش ستون‌ها در جدول اصلی کاربران
    list_display = ('username', 'phone_number', 'is_staff', 'is_active')
    
    # اضافه کردن فیلد شماره همراه به صفحه ویرایش کاربر در پنل ادمین
    fieldsets = UserAdmin.fieldsets + (
        ('اطلاعات بیشتر', {'fields': ('phone_number',)}),
    )