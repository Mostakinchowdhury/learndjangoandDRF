from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Order(models.Model):
  user_name=models.ForeignKey(User,on_delete=models.CASCADE,related_name="orders",related_query_name="order_field")
  orders_items=models.TextField()
  order_add_time=models.DateTimeField(auto_now_add=True)
  orders_quantity=models.IntegerField()

  def __str__(self):
        return f"Setting for {self.user_name.username}"
class Tag(models.Model):
  tag_name=models.CharField(max_length=200)
  tag_author=models.ForeignKey(User,related_name="tags",related_query_name="tags_field",on_delete=models.CASCADE)
  tag_add_time=models.DateTimeField(auto_now_add=True)
  def __str__(self):
    return self.tag_name
  # def getproducts(self):
  #       return ",".join([str(product) for product in self.used_product])

class Products_detail(models.Model):
  product_name=models.CharField(max_length=100)
  product_price=models.DecimalField(max_digits=10,decimal_places=2,default=0.00)
  product_type=models.CharField(max_length=80)
  product_description=models.TextField()
  adding_date=models.DateTimeField(auto_now_add=True)
  last_update=models.DateTimeField(auto_now=True)
  like_quantity=models.IntegerField()
  product_tags=models.ManyToManyField(Tag,related_name="used_product",related_query_name="used_product_field")

  def __str__(self):
    return self.product_name
  def gettags(self):
        return ",".join([str(product) for product in self.product_tags.all()])

class Setting(models.Model):
  user=models.OneToOneField(User,related_name="setting",related_query_name="setting_field",on_delete=models.CASCADE)
  theme=models.CharField(max_length=100)
  language=models.CharField(max_length=200)
  privacy=models.CharField(max_length=100)
  setting_add_time=models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return f"Setting for {self.user.username}"
