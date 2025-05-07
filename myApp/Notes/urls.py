from django.urls import path
from .views import AddNotesView,EditNotesView,UpdateNotesView,DeleteNotesView,ViewNotesView

urlpatterns = [
    path('notes', AddNotesView.as_view(), name='add-notes'),
    path('notes/<int:id>', EditNotesView.as_view(), name='edit-notes'),
    path('update-notes/<int:id>', UpdateNotesView.as_view(), name='update-notes'),
    path('delete-notes/<int:id>', DeleteNotesView.as_view(), name='delete-notes'),
    path('view-notes', ViewNotesView.as_view(), name='view-notes'),   
]
