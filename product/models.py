from django.db import models

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='images/')
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.title

 
class Product(models.Model):
    AVAILABLE =(
        ('In Stock', 'In Stock'),
        ('Out Of Stock', 'Out Of Stock'),
        ('Restocked', 'Restocked'),
    )
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    title = models.CharField(max_length=150, blank=True)
    description = models.CharField(max_length=255)
    image= models.ImageField(blank=True, upload_to='images/')
    price = models.FloatField(null=True, blank=True)
    # discount_price= models.FloatField(blank=True, null=True)
    available= models.CharField(choices=AVAILABLE, max_length=15, default='In Stock')
    max_quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    # amount = models.IntegerField(null=True, blank=True)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(blank=True)
    latest = models.BooleanField(blank=True)
   
    
    def __str__(self):
        return self.title
    
  


