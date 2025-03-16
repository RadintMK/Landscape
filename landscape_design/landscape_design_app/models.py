from django.db import models

class PortfolioProject(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='portfolio/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    

class BlogPost(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
class Service(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    price_from = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Цена от")
    image = models.ImageField(upload_to='service_images/')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.title

