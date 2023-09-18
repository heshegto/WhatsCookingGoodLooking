from django.db import models


class ReceiptStep(models.Model):
    receipt_name = models.CharField(max_length=128)
    step_number = models.PositiveSmallIntegerField(default=1)
    required_elements = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    next_step = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)
    time_to_cook = models.TimeField()
    is_last = models.BooleanField(default=True)

    def __str__(self):
        return f'Рецепт: {self.receipt_name} | Шаг приготовления: {self.step_number} | id: ({self.pk})'
