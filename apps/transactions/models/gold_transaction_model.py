from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
from decimal import Decimal

class GoldTransactionModel(models.Model):
    """
    مدل تراکنش‌های طلا برای سامانه Tajala_GOLD.
    این مدل بدون وضعیت (ثبت قطعی)، غیرقابل ویرایش مالی و دارای حذف نرم (deleted_at) است.
    """
    
    TRANSACTION_TYPES = [
        ('DEPOSIT', 'واریز (افزایش موجودی طلا)'),
        ('WITHDRAWAL', 'برداشت (کاهش موجودی طلا)'),
    ]

    # ارتباط با مشتری (فقط کاربران با نقش customer)
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.PROTECT,
        related_name='gold_transactions',
        limit_choices_to={'role': 'customer'},
        verbose_name="مشتری"
    )

    # نوع تراکنش (واریز یا برداشت)
    transaction_type = models.CharField(
        max_length=10,
        choices=TRANSACTION_TYPES,
        verbose_name="نوع تراکنش"
    )

    # وزن طلا به گرم با دقت ۴ رقم اعشار (مثال: ۱.۲۳۴۵ گرم)
    gold_weight = models.DecimalField(
        max_digits=12,
        decimal_places=4,
        validators=[MinValueValidator(Decimal('0.0001'))],
        verbose_name="وزن طلا (گرم)"
    )

    # قیمت هر گرم طلا در لحظه انجام تراکنش به ریال
    gold_price_per_gram = models.DecimalField(
        max_digits=15,
        decimal_places=0,
        verbose_name="قیمت هر گرم طلا (ریال)"
    )

    # ثبت‌کننده تراکنش (فقط مدیران سیستم)
    recorded_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='recorded_transactions',
        limit_choices_to={'role': 'admin'},
        verbose_name="ثبت‌کننده (مدیر)"
    )

    # توضیحات تکمیلی تراکنش
    description = models.TextField(
        blank=True,
        null=True,
        verbose_name="توضیحات"
    )

    # زمان ایجاد تراکنش (تاریخ فاکتور یا ثبت در سیستم)
    created_at = models.DateTimeField(
        auto_now_add=True, 
        verbose_name="زمان ایجاد"
    )

    # زمان حذف نرم (اگر مقدار داشته باشد یعنی تراکنش حذف شده است)
    deleted_at = models.DateTimeField(
        null=True,
        blank=True,
        verbose_name="زمان حذف"
    )

    class Meta:
        verbose_name = "تراکنش طلا"
        verbose_name_plural = "تراکنش‌های طلا"
        ordering = ['-created_at']

    def __str__(self):
        user_display = self.user.get_full_name() if self.user.get_full_name() else self.user.phone_number
        deleted_tag = " [حذف شده]" if self.deleted_at else ""
        return f"{user_display} - {self.get_transaction_type_display()} - {self.gold_weight}g{deleted_tag}"

    def save(self, *args, **kwargs):
        """
        مکانیزم امنیتی برای جلوگیری از هرگونه ویرایش پس از اولین ثبت دیتابیس.
        در این ساختار جدید، حتی توضیحات هم قفل می‌شود تا فاکتور کاملاً دست‌نخورده بماند.
        """
        if self.pk:  # اگر رکورد از قبل وجود داشته باشد (تلاش برای آپدیت)
            original = GoldTransaction.objects.get(pk=self.pk)
            
            # اگر ادمین دکمه حذف را زده باشد، فقط فیلد deleted_at تغییر می‌کند که مجاز است.
            # اما بقیه فیلدها نباید تحت هیچ شرایطی تغییر کنند.
            if (self.user_id != original.user_id or 
                self.transaction_type != original.transaction_type or 
                self.gold_weight != original.gold_weight or 
                self.gold_price_per_gram != original.gold_price_per_gram or
                self.description != original.description):
                raise ValidationError("تراکنش‌های ثبت شده کاملاً قطعی و غیرقابل ویرایش هستند. در صورت خطا، آن را حذف نرم کنید.")
                
        super().save(*args, **kwargs)

    def delete(self, *args, **kwargs):
        """
        تبدیل حذف فیزیکی به حذف نرم با ثبت زمان دقیق حذف.
        """
        self.deleted_at = timezone.now()
        self.save()