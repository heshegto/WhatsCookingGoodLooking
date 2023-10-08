from django.contrib import admin
from cooking.models import ReceiptStep, Receipt, StepsQueue
# Register your models here.

admin.site.register(ReceiptStep)


class StepsQueueAdmin(admin.TabularInline):
    model = StepsQueue
    fk_name = 'from_receipt'
    fields = ('to_step', 'position_in_queue')
    extra = 0


@admin.register(Receipt)
class ReceiptAdmin(admin.ModelAdmin):
    inlines = (StepsQueueAdmin,)
