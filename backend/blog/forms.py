from .models import Blogs
from django import forms

class Blogform(forms.ModelForm):
    class Meta:
      model=Blogs
      fields="__all__"
      labels={
        "blog_text":"Write your blog text",
      }
      widgets={
       "blog_owner":forms.HiddenInput(),
      }
    def __init__(self,*args, **kwargs):
       user=kwargs.pop("user",None)
       super().__init__(*args, **kwargs)
       self.fields["blog_owner"].initial=user


