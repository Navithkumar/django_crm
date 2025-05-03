from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import clientLogsSerializer
from .models import Client_logs
from rest_framework import status
from django.shortcuts import get_object_or_404
from CRM.common.pagination import MyCustomPagination
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q 

class AddClientsLogView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request,id=id):
        serializer = clientLogsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(
                admin_id = request.user.parent_id or None,
                handle_by = request.user.id,
                client_id = id
            )
            return Response({
                'is_v1':True,
                'status':True,
                'message':'Client_logs added successfully',
            })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateClientsLogViews(APIView):
    permission_classes = [IsAuthenticated]
    def patch(self, request,id=id):
        client_logs = get_object_or_404(Client_logs, id=id)
        serializer = clientLogsSerializer(client_logs, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'Client_logs updated Successfully',
                })
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ViewClientLogsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request,id=id):
        clients_log = Client_logs.objects.filter(client_id=id)
        if clients_log.exists():
            paginator = MyCustomPagination()
            result_page = paginator.paginate_queryset(clients_log, request)
            serializer = clientLogsSerializer(result_page, many=True)
            return paginator.get_paginated_response(serializer.data)
        else:
            return Response({
                    'is_v1':True,
                    'status':True,
                    'message':'No clients Found',
                })

