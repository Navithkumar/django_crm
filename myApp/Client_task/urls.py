from django.urls import path
from .views import AddTaskView,EditTaskView,UpdateTaskView,DeleteTaskView,ViewTaskView,AssignTaskView

urlpatterns = [
    path('task', AddTaskView.as_view(), name='add-task'),
    path('task/<int:id>', EditTaskView.as_view(), name='edit-task'),
    path('update-task/<int:id>', UpdateTaskView.as_view(), name='update-task'),
    path('delete-task/<int:id>', DeleteTaskView.as_view(), name='delete-task'),
    path('view-task', ViewTaskView.as_view(), name='view-task'),   
    path('assign-task/<int:id>', AssignTaskView.as_view(), name='assign-task'),
]
