from django.urls import path
from .views import AddClientsLogView,UpdateClientsLogViews,ViewClientLogsView

urlpatterns = [
    path('add-client-logs/<int:id>', AddClientsLogView.as_view(), name='add-client-log'),
    path('view-clients-logs/<int:id>', ViewClientLogsView.as_view(), name='view-client-log'),
    path('update-clients-logs/<int:id>', UpdateClientsLogViews.as_view(), name='update-client-log'),
]
