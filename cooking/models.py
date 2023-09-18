from django.db import models


class RecieptStep(models.Model):
    name = models.CharField(max_length=128)
    description = models.TextField(null=True, blank=True)
    required_elements = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images')
    category = models.ForeignKey('self', on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return f'Продукт: {self.name} | Категория: {self.category.name} | id: ({self.pk})'
