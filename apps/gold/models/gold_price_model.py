from django.db import models

class GoldPrice(models.Model):
    price = models.DecimalField(max_digits=12, decimal_places=2, verbose_name="قیمت") 
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="زمان ثبت در سیستم")

    class Meta:
        app_label = 'gold'
        verbose_name = "قیمت طلا"
        verbose_name_plural = "تاریخچه قیمت طلا"
        ordering = ['-created_at'] 

    def __str__(self):
        return f"{self.price} ({self.created_at.strftime('%H:%M:%S')})"