from django.db import models
from apps.common.models import BaseModel


class Client(BaseModel):

    name = models.CharField(max_length=255)
    physical_address = models.CharField(max_length=255)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=20, null=True, blank=True)

    def __str__(self):
        return self.name