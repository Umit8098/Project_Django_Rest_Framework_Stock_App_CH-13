from django.db import models
from django.contrib.auth.models import User

# ---------------------------------
# FixModel
# ---------------------------------

class FixModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

# ---------------------------------
# Models
# ---------------------------------
class Category(FixModel):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Brand(FixModel):
    name = models.CharField(max_length=64, unique=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class Product(FixModel):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category_products')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_products')
    name = models.CharField(max_length=128, unique=True)
    stock = models.SmallIntegerField(blank=True, default=0)

    def __str__(self):
        return f'{self.category} - {self.brand} - {self.name} # {self.stock}'


class Firm(FixModel):
    name = models.CharField(max_length=64)
    phone = models.CharField(max_length=16, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)

    def __str__(self):
        return f'{self.name} {self.phone}'
    

class Purchase(FixModel):
    firm = models.ForeignKey(Firm, on_delete=models.SET_NULL, null=True, related_name='firm_purchases')
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_purchases')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_purchases')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.product} [+{self.quantity}]'
    
    # insert/update:
    def save(self, *args, **kwargs):

        # Ürün getir:
        product = Product.objects.get(id=self.product_id)
        
        if (self.id): # update/product miktarı güncelleme işlemi
            old_quantity = Purchase.objects.get(id=self.id).quantity
            new_quantity = self.quantity - old_quantity
        else: # insert/yeni satın alma işlemi
            new_quantity = self.quantity
                
        # Ürün stok bilgi güncelle:
        product.stock += new_quantity
        # Ürün kaydet:
        product.save()
        
        return super().save(*args, **kwargs)
    
    # delete:
    def delete(self, *args, **kwargs):
        # Ürün getir:
        product = Product.objects.get(id=self.product_id)
        # Ürün stok bilgi güncelle:
        product.stock -= self.quantity
        # Ürün kaydet:
        product.save()
        return super().delete(*args, **kwargs)



class Sale(FixModel):
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, related_name='brand_sales')
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='product_sales')
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    price_total = models.DecimalField(max_digits=8, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return f'{self.product} [-{self.quantity}]'

    # insert/update:
    def save(self, *args, **kwargs):

        # Ürün getir:
        product = Product.objects.get(id=self.product_id)
        
        # Miktar yeterli mi?
        if (product.stock >= self.quantity):
            if (self.id): # update/product miktarı güncelleme işlemi
                old_quantity = Sale.objects.get(id=self.id).quantity
                new_quantity = self.quantity - old_quantity
            else: # insert/yeni satın alma işlemi
                new_quantity = self.quantity
                
            # Ürün stok bilgi güncelle:
            product.stock -= new_quantity
            # Ürün kaydet:
            product.save()
        
            return super().save(*args, **kwargs)
        
        else:
            from django.core.exceptions import ValidationError
            raise ValidationError(f'Dont have enough stock. Current stock is {product.stock}')
            
    # delete:
    def delete(self, *args, **kwargs):
        # Ürün getir:
        product = Product.objects.get(id=self.product_id)
        # Ürün stok bilgi güncelle:
        product.stock += self.quantity
        # Ürün kaydet:
        product.save()
        return super().delete(*args, **kwargs)
