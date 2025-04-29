from django.urls import path
from .views import RegisterView, LoginView,UserListingView,UserUpdateView,UserListById,DeleteUserView

urlpatterns = [
    path('register', RegisterView.as_view(), name='register'),
    path('login', LoginView.as_view(), name='login'),
    path('user', UserListingView.as_view(), name='user-listing'),
    path('user/<int:id>', UserUpdateView.as_view(), name='user-update'),
    path('list-user/<int:id>',UserListById.as_view(),name = 'list-user'),
    path('delete-user/<int:id>',DeleteUserView.as_view(),name = 'delete-user')
]
