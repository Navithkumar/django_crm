from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import NotesSerializer
from myApp.Notification.serializers import NotificationSerializer
from .models import UserNotes
from rest_framework import status
from django.shortcuts import get_object_or_404
from CRM.common.pagination import MyCustomPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q 

class AddNotesView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = NotesSerializer(data = request.data)
        user = request.user
        if serializer.is_valid():
            serializer.save(
                client_id = request.data.get('client_id'),
                user_id = user.id,
            )
            return Response({
                'is_v1':True,
                'status':True,
                'message':'Notes added successfully',
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditNotesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id=id):
        task = get_object_or_404(UserNotes,id=id)
        serializer = NotesSerializer(task)
        if serializer:
            return Response({
                    'is_v1':True,
                    'status':True,
                    'data':serializer.data,
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateNotesView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self,request,id=id):
        task = get_object_or_404(UserNotes,id=id)
        serializer = NotesSerializer(task,data =request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'Notes updated Successfully',
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteNotesView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,id=id):
        task = get_object_or_404(UserNotes,id=id)
        task.delete()
        return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'Task Deleted Successfully',
                })

class ViewNotesView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        user = request.user
        task = UserNotes.objects.filter(Q(user_id = user.id))
        paginator = MyCustomPagination()
        result = paginator.paginate_queryset(task,request)
        serializer = NotesSerializer(result,many=True)
        if serializer:
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'No Notes Found',
                })