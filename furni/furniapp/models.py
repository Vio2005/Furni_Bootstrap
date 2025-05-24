from django.db import models

# Create your models here.
class Chair(models.Model):
    name=models.CharField(max_length=100)
    photo=models.ImageField(upload_to='photo')
    price=models.PositiveIntegerField()
    def __str__(self):
        return self.name
    

class Cart(models.Model):
    total=models.PositiveIntegerField(default=0)
    date=models.DateField(auto_now_add=True)
    def __str__(self):
        return str(self.id)

class CartProduct(models.Model):
    cart=models.ForeignKey(Cart,on_delete=models.CASCADE)
    product=models.ForeignKey(Chair,on_delete=models.CASCADE)
    qty=models.PositiveIntegerField(default=0)
    amount=models.PositiveIntegerField(default=0)
    def __str__(self):
        return f"invoice no-{self.cart}---{self.product}"
