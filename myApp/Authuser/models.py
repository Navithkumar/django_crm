from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.db import models

class UserManager(BaseUserManager):
    def create_user(self, username, email, is_admin=0, is_super_admin=0, password=None, status=1, parent_id=None):
        if not email:
            raise ValueError("Users must have an email address")
        email = self.normalize_email(email)
        user = self.model(
            username=username,
            email=email,
            status=status,
            is_admin=is_admin,
            is_super_admin=is_super_admin,
            parent_id=parent_id
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=100, unique=True)
    email = models.EmailField(unique=True)
    status = models.IntegerField(default=1)
    is_admin = models.IntegerField(default=0)
    is_super_admin = models.IntegerField(default=0)
    parent_id = models.IntegerField(null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    objects = UserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'is_admin']

    def __str__(self):
        return self.username
