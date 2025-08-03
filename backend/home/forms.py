from django import forms
from .models import Products_detail
from .models import CustomUser

class customuserform(forms.ModelForm):
    class Meta:
      model=CustomUser
      fields="__all__"

class Productform(forms.ModelForm):
  class Meta:
    model=Products_detail
    fields="__all__"
    readonly="product_like"
  def __init__(self, *args, **kwargs):
     super(Productform, self).__init__(*args, **kwargs)
     self.fields['like_quantity'].disabled = True

class Myform(forms.Form):
  username=forms.CharField(label="Enter your password",widget=forms.TextInput(attrs={"class":"forminput","placeholder":"Enter your username in here"}))
  password=forms.CharField(label="Enter your password",widget=forms.PasswordInput(attrs={"class":"forminput","placeholder":"Enter your password in here"}))
  passwordsecond=forms.CharField(label="Retype your password",widget=forms.PasswordInput(attrs={"class":"forminput","placeholder":"Retype password ensure"}))

  def clean_username(self):
      validetusername = self.cleaned_data["username"]
      invalidusername=[""," ","username","user","name","admin"]
      if validetusername in invalidusername:
        raise forms.ValidationError("Invalid username this username not acceptable") #django auto detect field to bind error and break form validation
      return validetusername
  def clean(self):
     clean_data= super().clean()
     fpawwsord=clean_data["password"]
     spawwsord=clean_data["passwordsecond"]
     if fpawwsord!=spawwsord:
       self.add_error("passwordsecond","password doesnot match please ensure")  #--- #two field valid in here django unable to detect whice field's error this is.that's why need to add error to push error a specic field error dict.but form continew validate another fields
       #raise forms.ValidationError("password doesn't match") #~~~~~ #its a form wide error becouse django unable to detect field becouse many field in here not specic it clean method not clean_field method that's why its not error for a specic field error dict error but also its a whole form's wide error and its break form validation and other fields error





