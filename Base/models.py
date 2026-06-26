from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    category = models.CharField(max_length=20)
    
    def __str__(self):
        return self.category

class Product(models.Model):
    name = models.CharField(max_length=200)
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )
    price = models.IntegerField()

class Item(models.Model):
    name = models.CharField(max_length=20, null=True)

    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,  null=True
    )

    rasm = models.ImageField(null=True, upload_to='media')

    rasm_2 = models.ImageField(null=True, blank=True)
    rasm_3 = models.ImageField(null=True, blank=True)
    rasm_4 = models.ImageField(null=True, blank=True)
    rasm_5 = models.ImageField(null=True, blank=True)
    rasm_6 = models.ImageField(null=True, blank=True)
    rasm_7 = models.ImageField(null=True, blank=True)
    rasm_8 = models.ImageField(null=True, blank=True)
    rasm_9 = models.ImageField(null=True, blank=True)
    rasm_10 = models.ImageField(null=True, blank=True)
    rasm_11 = models.ImageField(null=True, blank=True)
    rasm_12 = models.ImageField(null=True, blank=True)

    narxi = models.IntegerField( null=True)
    skidkasi = models.CharField(max_length=100,  null=True)
    tavsifi = models.TextField(null=True, blank=True)
    
class Men(models.Model):
    category1 = models.ForeignKey("Category", on_delete=models.CASCADE, null=True)
    rasm1 = models.ImageField(upload_to='media')
    narxi1 = models.IntegerField()
    skidkasi1 = models.IntegerField()
    tavsifi1 = models.CharField(max_length=100)

    def __str__(self):
        return self.tavsifi1
    
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class CartItem(models.Model):
    cart = models.ForeignKey(
        Cart,
        on_delete=models.CASCADE
    )

    item = models.ForeignKey(
        Item,
        on_delete=models.CASCADE
    )

    quantity = models.PositiveIntegerField(default=1)
    
    
class Main_branch(models.Model):
    picture = models.ImageField(upload_to="media")
    desc = models.TextField(blank=True)

    def __str__(self):
        return self.desc
    
class Contact(models.Model):
    name = models.CharField(max_length=200)
    text = models.TextField()
    
# foreginKey ---- boshqa model