from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import RegisterSerializer, LoginSerializer
from .models import User
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from CRM.common.pagination import MyCustomPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q 

class RegisterView(APIView):

    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                'is_v1':True,
                'status':True,
                'message':'User registered successfully',
            });
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            user = serializer.validated_data['user']
            is_admin = serializer.validated_data['is_admin']

            refresh = RefreshToken.for_user(user)
            access_token = str(refresh.access_token)
            refresh_token = str(refresh)
            
            return Response({
                'is_v1': True,
                'status': True,
                'message': 'Admin login successful' if is_admin else 'User login successful',
                'is_admin': is_admin,
                'access': access_token,
            }, status=status.HTTP_200_OK)

class UserListingView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user  
        
        if user.is_super_admin == 1: 
            users = User.objects.exclude(is_super_admin=1)
        else: 
            users = User.objects.filter(
    ( (Q(id=user.id) | Q(parent_id=user.id)) & Q(is_admin=0)))

        
        paginator = MyCustomPagination()
        result_page = paginator.paginate_queryset(users, request)
        serializer = RegisterSerializer(result_page,many=True)
        if(serializer):
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'No clients Found',
                })

class UserUpdateView(APIView):
    def patch(self,request,id):
        users = get_object_or_404(User,id=id)
        serializer = RegisterSerializer(users,partial=True,data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'User updated Successfully',
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserListById(APIView):
    def get(self,request,id):
        users = get_object_or_404(User,id=id)
        serializer = RegisterSerializer(users)
        if serializer:
            return Response({
                    'is_v1':True,
                    'status':True,
                    'data':serializer.data,
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteUserView(APIView):
    def delete(self,request,id):
        users = get_object_or_404(User,id=id)
        users.delete()
        return Response({
            'is_v1':True,
            'status':True,
            'message':'User Deleted Successfully',
        })