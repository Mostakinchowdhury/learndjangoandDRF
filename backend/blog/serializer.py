# blog/serializers.py
from .models import Blogs,Comment
from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model

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
    return user


class loginserializer(serializers.Serializer):
  email=serializers.EmailField()
  password=serializers.CharField()

  def validate(self, data):
    email=data.get("email")
    password=data.get("password")
    user=authenticate(email=email,password=password)
    if user==None:
      raise serializers.ValidationError("not match")
    data['user']=user
    return data






