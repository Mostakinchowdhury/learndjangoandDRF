from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.

class Blogs(models.Model):
  blog_owner=models.ForeignKey(User,on_delete=models.CASCADE,related_name="blogs")
  blog_text=models.TextField()
  blog_img=models.ImageField(upload_to="blogs", blank=True,null=True)
  blog_upload_time=models.DateTimeField(auto_now_add=True)
  blog_last_upload_time=models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.blog_text



class Comment(models.Model):
  blog=models.ForeignKey(Blogs,on_delete=models.CASCADE,related_name="coments")
  coment_text=models.TextField(max_length=300)
  coment_date=models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.blog.__str__()

