from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TaskSerializer
from .models import ClientTask
from rest_framework import status
from django.shortcuts import get_object_or_404
from CRM.common.pagination import MyCustomPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q 

class AddTaskView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request):
        serializer = TaskSerializer(data = request.data)
        user = request.user
        if serializer.is_valid():
            serializer.save(
                assigned_by = request.user.id,
            )
            return Response({
                'is_v1':True,
                'status':True,
                'message':'Task added successfully',
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class EditTaskView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id=id):
        task = get_object_or_404(ClientTask,id=id)
        serializer = TaskSerializer(task)
        if serializer:
            return Response({
                    'is_v1':True,
                    'status':True,
                    'data':serializer.data,
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateTaskView(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self,request,id=id):
        task = get_object_or_404(ClientTask,id=id)
        serializer = TaskSerializer(task,data =request.data, partial = True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'Task updated Successfully',
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteTaskView(APIView):
    permission_classes = [IsAuthenticated]
    def delete(self,request,id=id):
        task = get_object_or_404(ClientTask,id=id)
        task.delete()
        return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'Task Deleted Successfully',
                })

class ViewTaskView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        
        user = request.user
        if user.is_super_admin ==1:
            task = ClientTask.objects.all()
        elif user.is_admin ==1:
            task = ClientTask.objects.filter(Q(assigned_by = user.id))
        else:
            task = ClientTask.objects.filter(Q(assigned_to = user.id))
        
        paginator = MyCustomPagination()
        result = paginator.paginate_queryset(task,request)
        serializer = TaskSerializer(result,many=True)
        if serializer:
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'No Task Found',
                })
        
class AssignTaskView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self,request,id=id):
        user = request.user
        data = request.data

        if user.is_super_admin == 1 or user.is_admin == 1:
            task = ClientTask.objects.filter(
                id=id
            ).first()
            if not task:
                return Response({
                    'is_v1':False,
                    'status': False,
                    'message': 'Task not found or already assigned'
                })

            task.assigned_by = user.id
            task.assigned_to = data.get('assigned_to', task.assigned_to)
            task.deadline = data.get('deadline', task.deadline)
            task.priority = data.get('priority', task.priority)
            task.task_status = data.get('task_status', task.task_status)
            task.save()

            return Response({
                'is_v1':True,
                'status': True,
                'message': 'Task updated successfully'
            })
        else:
            return Response({
                'is_v1':False,
                'status': False,
                'message': []
            })