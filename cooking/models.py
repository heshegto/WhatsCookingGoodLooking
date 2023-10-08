from django.db import models


class ReceiptStep(models.Model):
    name = models.CharField(max_length=128)
    required_elements = models.TextField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to='product_images', null=True, blank=True)
    time_to_cook = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f'Step: {self.name} || id: ({self.pk})'

    def __repr__(self):
        return f'Step: {self.name} || id: ({self.pk})'


class Receipt(ReceiptStep):
    steps = models.ManyToManyField(to='ReceiptStep', related_name='steps', through='StepsQueue', blank=True)

    def __str__(self):
        return f'Recipt: {self.name} || id: ({self.pk})'

    def __repr__(self):
        return f'Recipt: {self.name} || id: ({self.pk})'


class StepsQueue(models.Model):
    from_receipt = models.ForeignKey(to=Receipt, on_delete=models.CASCADE, null=False, blank=False, related_name='from_reciept')
    to_step = models.ForeignKey(to=ReceiptStep,  on_delete=models.CASCADE, null=False, blank=False, related_name='to_step')
    position_in_queue = models.PositiveSmallIntegerField(default=1)

    class Meta:
        unique_together = ('from_receipt', 'position_in_queue')
