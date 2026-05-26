from django.contrib.auth.models import AbstractUser
from django.db import models
from apps.common.models import BaseModel

class User(AbstractUser, BaseModel):

    class Roles(models.TextChoices):
        ADMIN = "ADMIN", "Admin"
        PROJECT_MANAGER = "PROJECT_MANAGER", "Project Manager"
        STORE_MANAGER = "STORE_MANAGER", "Store Manager"
        AUDITOR = "AUDITOR", "Auditor"
        USER = "USER", "User"

    email = models.EmailField(unique=True)
    
    phone_number = models.CharField(max_length=20, null=True, blank=True)
    
    role = models.CharField(
        max_length=50,
        choices=Roles.choices,
        default=Roles.USER
    )

    is_verified = models.BooleanField(default=False)
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]

    def __str__(self):
        return self.email