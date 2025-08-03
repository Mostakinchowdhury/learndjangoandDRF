from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.

class Blogs(models.Model):
  blog_owner=models.ForeignKey(User,on_delete=models.CASCADE)
  blog_text=models.TextField()
  blog_img=models.ImageField(upload_to="blogs", blank=True,null=True)
  blog_upload_time=models.DateTimeField(auto_now_add=True)
  blog_last_upload_time=models.DateTimeField(auto_now=True)

