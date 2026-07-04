from django.db import models
from apps.common.models import BaseModel
from apps.accounts.models import User
from apps.clients.models import Client

class Project(BaseModel):

    class Roles(models.TextChoices):
        DRAFT = "DRAFT", "Draft"
        ACTIVE = "ACTIVE", "Active"
        COMPLETED = "COMPLETED", "Completed"
        CANCELLED = "CANCELLED", "Cancelled"

    name = models.CharField(max_length=255)
    description = models.TextField()
    client = models.ForeignKey(
        Client,
        on_delete=models.SET_NULL,
        null=True,
        related_name='clients'
    )
    location = models.CharField(max_length=255) #The location has to be improved Later

    start_date = models.DateField()
    end_date = models.DateField()

    supervisor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='supervisor'
    )
    status = models.CharField(
        max_length=50,
        choices=Roles.choices,
        default=Roles.DRAFT
    )


    def __str__(self):
        return f"{self.name} ({self.status}) {self.client.name}"