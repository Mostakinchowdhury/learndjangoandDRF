from django.db import models
from .manager import myUserManager
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    GENDER_CHOICES = (
        ('male', 'Male'),
        ('female', 'Female'),
        ('others', 'Others'),
    )
    email = models.EmailField(unique=True)
    phone_num=models.CharField(max_length=20)
    country_name=models.CharField(max_length=30)
    bio=models.TextField(max_length=320)
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES, default='male')
    profile_image=models.ImageField(upload_to="profiles/",blank=True,null=True)
    USERNAME_FIELD="email"
    EMAIL_FIELD="email"
    REQUIRED_FIELDS = ["username",'phone_num']
    objects=myUserManager()

    def __str__(self):
       return self.email

class Order(models.Model):
  user_name=models.ForeignKey(CustomUser,on_delete=models.CASCADE,related_name="orders",related_query_name="order_field")
  orders_items=models.TextField()
  order_add_time=models.DateTimeField(auto_now_add=True)
  orders_quantity=models.IntegerField()

  def __str__(self):
        return f"Setting for {self.user_name.username}"
class Tag(models.Model):
  tag_name=models.CharField(max_length=200)
  tag_author=models.ForeignKey(CustomUser,related_name="tags",related_query_name="tags_field",on_delete=models.CASCADE)
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
  user=models.OneToOneField(CustomUser,related_name="setting",related_query_name="setting_field",on_delete=models.CASCADE)
  theme=models.CharField(max_length=100)
  language=models.CharField(max_length=200)
  privacy=models.CharField(max_length=100)
  setting_add_time=models.DateTimeField(auto_now_add=True)

  def __str__(self):
        return f"Setting for {self.user.username}"




