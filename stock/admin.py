from django.contrib import admin
from .models import (
    Category,
    Brand,
    Product,
    Firm,
    Purchase,
    Sale,
)

# Register your models here.
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(Product)
admin.site.register(Firm)
admin.site.register(Purchase)
admin.site.register(Sale)
