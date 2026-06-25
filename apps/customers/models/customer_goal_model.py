from django.db import models
from customers import models as customers_models
from products import models as products_models

class CustomerGoalModel(models.Model):
    """
    مدل اهداف خرید مشتری (محصولات نشان‌شده برای ویترین داشبورد)
    """
    customer = models.ForeignKey(
        customers_models.CustomerModel,
        on_delete=models.CASCADE,
        related_name='goals',
        verbose_name="مشتری"
    )
    product = models.ForeignKey(
        products_models.ProductModel,
        on_delete=models.CASCADE,
        related_name='targeted_by',
        verbose_name="محصول هدف"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ نشان کردن")

    class Meta:
        verbose_name = "هدف خرید مشتری"
        verbose_name_plural = "اهداف خرید مشتریان"
        # جلوگیری از ثبت تکراری یک محصول برای یک مشتری
        unique_together = ('customer', 'product')

    def __str__(self):
        return f"{self.customer.full_name} -> {self.product.title}"