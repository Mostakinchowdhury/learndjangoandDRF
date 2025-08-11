# blog/serializers.py
from .models import Blogs,Comment
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.exceptions import AuthenticationFailed

def get_tokens_for_user(user):
    if not user.is_active:
      raise AuthenticationFailed("User is not active")

    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

User = get_user_model()



def valideproductname(value):
  invalid_name=['kichuna','demo','none']
  if value in invalid_name:
    raise serializers.ValidationError("sorry product name invalid")

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'
        extra_kwargs = {
          "blog_text":{
            "validators":[valideproductname]
          }
        }
class ComentSerializer(serializers.ModelSerializer):
    class Meta:
        model =Comment
        fields = '__all__'

def validename(value):
  invalid_name=['name','fname','lname','',' ','nam']
  if value in invalid_name:
    raise serializers.ValidationError("You entered a invalid name")

def namelength(value):
  if len(value)<4:
      raise serializers.ValidationError("Sorry your name too short")

class Myserializer(serializers.Serializer):
  fullname=serializers.CharField(max_length=20,label="enter name",validators=[validename,namelength])
  age=serializers.IntegerField()
  proffesion=serializers.CharField(max_length=100)


  def validate_age(self,value):
    if value<18:
      raise serializers.ValidationError("You are so teenagers bro ")
    return value

  def validate(self, data):
    admin=['mostakin','rubel','moriyom',]
    name=data["fullname"].lower()
    age=data["age"]
    proffesion=data["proffesion"].lower()
    if name in admin and proffesion=="software engineer":
      raise serializers.ValidationError({'fullname':"sorry you are admin"})
    elif name == 'mohir ali' and age >40:
      raise serializers.ValidationError("You are the father of admins")
    return data


class registerserializer(serializers.ModelSerializer):
  password=serializers.CharField(write_only=True)
  class Meta:
    model=User
    fields=["email","phone_num","password","username"]

  def create(self, validated_data):
    user=User(email=validated_data['email'],username=validated_data["username"],phone_num=validated_data['phone_num'])
    user.set_password(validated_data.get("password"))
    user.save()
    tokens=get_tokens_for_user(user)
    return {'token':tokens}


class loginserializer(serializers.Serializer):
  password=serializers.CharField(min_length=8)
  email=serializers.EmailField()
  def validate(self, attrs):
     user=authenticate(email=attrs['email'],password=attrs['password'])
     if user is not None:
       attrs['token']=get_tokens_for_user(user)
     else:
       raise serializers.ValidationError("Your information not match with any record try again")

     return attrs

class ChangePasswordSerializer(serializers.Serializer):
    old_password = serializers.CharField(write_only=True)
    new_password = serializers.CharField(write_only=True)
    confirm_password = serializers.CharField(write_only=True)

    def validate_new_password(self, value):
        if len(value) < 8:
            raise serializers.ValidationError("Password must be at least 8 characters long")
        return value

    def validate(self, attrs):
        user = self.context.get('user')
        old_password = attrs.get('old_password')
        new_password = attrs.get('new_password')
        confirm_password = attrs.get('confirm_password')

        if new_password != confirm_password:
            raise serializers.ValidationError("New password and confirm password do not match")

        if not user.check_password(old_password):
            raise serializers.ValidationError("Old password is incorrect")

        return attrs

    def save(self, **kwargs):
        user = self.context.get('user')
        user.set_password(self.validated_data['new_password'])
        user.save()
        return user














