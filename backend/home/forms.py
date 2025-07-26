from django import forms
from .models import Products_detail
class Productform(forms.ModelForm):
  class Meta:
    model=Products_detail
    fields="__all__"
    readonly="product_like"
  def __init__(self, *args, **kwargs):
     super(Productform, self).__init__(*args, **kwargs)
     self.fields['like_quantity'].disabled = True
