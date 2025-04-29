from django.urls import path
from .views import AddClientView,ClientListing,ClientUpdateView,DeleteClientView,ClientListById

urlpatterns = [
    path('add-clients', AddClientView.as_view(), name='add-clients'),
    path('view-clients', ClientListing.as_view(), name='view-clients'),
    path('update-clients/<int:pk>', ClientUpdateView.as_view(), name='update-clients'),
    path('delete-client/<int:id>', DeleteClientView.as_view(), name='delete-client'),
    path('list-client/<int:id>', ClientListById.as_view(), name='list-client')
]
