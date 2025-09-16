import uuid
from django.db import models

class Product(models.Model):
    CATEGORY_CHOICES = [
        ('gear', 'Gear'),
        ('clothing', 'Clothing'),
        ('shoes', 'Shoes'),
        ('accessory', 'Accessory')
    ]
    
    name = models.CharField(max_length=255)
    price = models.PositiveIntegerField()
    description = models.TextField()
    thumbnail = models.URLField(blank=True, null=True)
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES, default='update')
    rating = models.FloatField(default=0)
    stock = models.PositiveIntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    @property
    def is_news_hot(self):
        return self.news_views > 20
        
    def increment_views(self):
        self.news_views += 1
        self.save()