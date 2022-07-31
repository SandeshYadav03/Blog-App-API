from contextvars import Token
from email.quoprimime import body_length
from functools import partial
from lib2to3.pgen2 import token
from logging import raiseExceptions
from msilib.schema import ODBCAttribute
from xml.etree.ElementTree import Comment
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


from django.http import JsonResponse
from . models import Blog, Comments
from .serializer import BlogSerializer, CommentModelSerializer, LoginSerializer
from rest_framework import status, authentication, permissions

# class APIViews(APIView):
    # serializer_class = BlogSerializer

    # def get(self,request, pk=None):
        # if pk:
            # try:
                # blog = Blog.objects.get(pk=pk)
                # serializer = self.serializer_class(blog)
                # return Response(serializer.data)
            # except Blog.DoesNotExist:
                # return Response({"details" : "Does Not Found"}, status = status.HTTP_404_NOT_FOUND)
        # else:
            # blogs = Blog.objects.all()
            # serializer = self.serializer_class(blogs, many=True)
            # return Response(serializer.data)
        # 

    # def post(self,request):
        # serializer = BlogSerializer(data=request.data)
        # serializers = self.serializer_class(data=request.data)
        # if serializer.is_valid():
            # title = serializer.validated_data.get('title')
            # post = serializer.validated_data.get('post')
            # date = serializer.validated_data.get('date')
            # Blog.objects.create(
                # title=title,
                # post=post,
                # date=date
            # )
            # return Response(serializer.data)
        # else:
            # return Response(serializer.errors)      
    #   

    # def put(self,request,pk=None):
        # 
        # if pk:
            # try:
                # blog = Blog.objects.get(id=pk)
                # serializers = self.serializer_class(blog, data=request.data)
                # if serializers.is_valid():
                    # title = serializers.validated_data.get('title')
                    # post = serializers.validated_data.get('post')
                    # date = serializers.validated_data.get('date')
                    # blog.title=title
                    # blog.post=post
                    # blog.date=date
                    # blog.save()
                    # return Response(serializers.data)
                # return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    
            # except:
                # return Response({'details' : 'Not Found'}, status = status.HTTP_404_NOT_FOUND)
        # return Response({'details' : 'id is not Provided'}, status=status.HTTP_400_BAD_REQUEST) 
        # 
        #    

    # def patch(self,request,pk=None):
    # 
        # try:
            # blog = Blog.objects.get(id=pk)
            # serializers = self.serializer_class(blog, data=request.data, partial=True)
            # if serializers.is_valid():
                # title = serializers.validated_data.get('title')
                # post = serializers.validated_data.get('post')
                # date = serializers.validated_data.get('date')
                # if title:
                    # blog.title=title
                # if post:
                    # blog.post=post
                # if date:
                    # blog.date=date
                # blog.save()
                # return Response(serializers.data)
            # return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)    
        # except:
            # return Response({'details' : 'Not Found'}, status = status.HTTP_404_NOT_FOUND)

#    

    # def delete(self,request,pk=None):

        # if pk:
            # try:
                # blog = Blog.objects.get(pk=pk)
                # blog.delete()
                # return Response({'details' : 'Deleted'})
            # except Blog.DoesNotExist:
                # return Response({'details' : 'Not Found...'}, status = status.HTTP_404_NOT_FOUND)
        # return Response({'details' : 'id is Not Provided'}, status=status.HTTP_400_BAD_REQUEST) 
 





from rest_framework import viewsets
from .serializer import BlogModelSerializer
from rest_framework.generics import get_object_or_404

from api import serializer

    
class BlogViewSetAPI(viewsets.ModelViewSet):

    serializer_class = BlogModelSerializer
    queryset = Blog.objects.all()

    # def list(self, request):
        # serializer = self.serializer_class(self.queryset,many=True)
        # return Response(serializer.data)

    # def create(self, request,):
        # serializer = self.serializer_class(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save() 
        # return Response(serializer.data) 

    # def retrieve(self, request,pk=None):
        # blog = get_object_or_404(self.queryset,pk=pk)
        # serializer = self.serializer_class(blog)
        # return Response(serializer.data)

    # def update(self, request, pk=None):
        # blog = get_object_or_404(self.queryset,pk=pk)
        # serializer = self.serializer_class(blog, data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data)

    # def partial_update(self, request, pk=None):
        # blog = get_object_or_404(self.queryset,pk=pk)
        # serializer = self.serializer_class(blog, data=request.data,partial=True)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        # return Response(serializer.data)

    # def delete(self, request, pk=None):
        # blog = get_object_or_404(self.queryset,pk=pk)
        # blog.delete()
        # return Response()

from .serializer import UserSerializer,LoginSerializer
from django.contrib.auth.models import User
class UserView(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    



from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings    
class LoginView(ObtainAuthToken):
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES


# from rest_framework.authtoken.models import Token
# from django.contrib.auth import authenticate
# class LoginView(APIView):
    # serializer_class = LoginSerializer
    # def post(self,request):
        # validate otp -- comment
        # serializer = self.serializer_class(data=request.POST)
        # if serializer.is_valid():
            # username = serializer.validated_data['username']
            # password = serializer.validated_data['password']
            # user = authenticate(username=username,password=password)
            # if user:
                # token, _ = Token.objects.get_or_create(user=user)
                # return Response({'token': token.key})
            # return Response({'details': 'No User Found'})
        # return Response(serializer.error)
            
from rest_framework import filters
from rest_framework.throttling import UserRateThrottle
from .permission import IsOwner
class BlogView(viewsets.ModelViewSet):
    throttle_classes = [UserRateThrottle]
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated,IsOwner]
    serializer_class = BlogModelSerializer
    queryset = Blog.objects.all()
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['title']
    ordering_fields = ['id','title', 'date']
    


class CommentView(viewsets.ModelViewSet):
    serializer_class = CommentModelSerializer
    queryset = Comments.objects.all()

    # def list(self,request):
        # sorting = request.GET.get('sorting')
        # order = request.GET.get('order')
        # filter = {}
        # if sorting:
            # Blog.objects.all().order_by(f'{order}{sorting}')
        # else:
            # Blog.objects.all() 