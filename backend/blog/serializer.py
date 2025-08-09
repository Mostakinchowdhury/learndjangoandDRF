# blog/serializers.py
from .models import Blogs,Comment
from rest_framework import serializers

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








