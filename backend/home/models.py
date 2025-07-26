from django.db import models

# Create your models here.
class Products_detail(models.Model):
  product_name=models.CharField(max_length=100)
  product_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
  product_type=models.CharField(max_length=80)
  product_description=models.TextField()
  adding_date=models.DateTimeField(auto_now_add=True)
  last_update=models.DateTimeField(auto_now=True)
  like_quantity=models.IntegerField()

  def __str__(self):
    return self.product_name
