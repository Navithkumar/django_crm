from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import clientSerializer
from .models import Client
from rest_framework import status
from django.shortcuts import get_object_or_404
from CRM.common.pagination import MyCustomPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q 

class AddClientView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = clientSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                user_id=request.user.id,
                parent_id=request.user.parent_id or None 
            )
            return Response({
                'is_v1':True,
                'status':True,
                'message':'Client added successfully',
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ClientListing(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        
        user = request.user
        if user.is_super_admin == 1:
            clients = Client.objects.all().order_by('-created_at')
        elif user.is_admin == 1:
            clients = Client.objects.filter(
                Q(user=user) | Q(parent=user)
            ).order_by('-created_at')
        else:
            clients = Client.objects.filter(user=user).order_by('-created_at')


        paginator = MyCustomPagination()
        result_page = paginator.paginate_queryset(clients, request)
        serializer = clientSerializer(result_page, many=True)
        if serializer:
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'No clients Found',
                })

class ClientUpdateView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self,request,pk):
        client = get_object_or_404(Client, pk=pk)
        serializer = clientSerializer(client, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'Client updated Successfully',
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteClientView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,id):
            client = get_object_or_404(Client, id=id)
            client.delete()
            return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'Client Deleted Successfully',
                })

class ClientListById(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id):
        client = get_object_or_404(Client, id=id)
        serializer = clientSerializer(client)
        if serializer:
            return Response({
                    'is_v1':True,
                    'status':True,
                    'data':serializer.data,
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)