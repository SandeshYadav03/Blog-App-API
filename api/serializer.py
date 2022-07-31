from dataclasses import fields
from pyexpat import model
from signal import valid_signals
from venv import create
from xml.etree.ElementTree import Comment
from rest_framework import serializers
from django.contrib.auth.models import User

from api.models import Blog, Comments

class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    post = serializers.CharField()
    date = serializers.DateField()


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

        extra_kwargs = {
            'password': {
                'write_only' : True
            }
        }


    def create(self, validated_data):
        print(validated_data)
       
        user = User.objects.create(
            username =  validated_data['username'],
            first_name =  validated_data['first_name'],
            last_name =  validated_data['last_name'],
            email =  validated_data['email'],            
        )
        if validated_data.get('password'):
           user.set_password(validated_data['password'])
           user.save()
           return validated_data

    def update(self, instance, validated_data):
        instance.set_password(validated_data['password'])
        instance.save()
        return validated_data

#For Comment
class CommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('comment','blog','id')
        depth = 1

class BlogCommentModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comments
        fields = ('comment',)        
 

#For Blog
class BlogModelSerializer(serializers.ModelSerializer):
    # comment = BlogCommentModelSerializer(many=True)
    class Meta:
        model = Blog
        fields = ('id','title','post','date','owner')
        depth = 1




class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField()



