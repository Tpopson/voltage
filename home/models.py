from django.db import models


# Create your models here.
STATUS = [
    ('New', 'New'),
    ('Pending', 'Pending'),
    ('Processing', 'Processing'),
    ('Sorted', 'Sorted'),
]
class Contact(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    message = models.TextField()
    admin_note = models.TextField()
    status = models.CharField(max_length=50, choices=STATUS, default='New')

    def __str__(self):
        return self.full_name

    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'

    
class Slide(models.Model):
    title = models.CharField(max_length=50)
    text = models.CharField(max_length=50)
    carousel = models.ImageField(upload_to='carousel', default='slide.jpg')

    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='product', default='prod.jpg')
    price = models.IntegerField()
    min = models.IntegerField(default=1)
    max = models.IntegerField()
    description = models.TextField()
    latest = models.BooleanField(default=False)
    featured = models.BooleanField(default=False)
    available = models.BooleanField(default=False)

    def __str__(self):
        return self.title


