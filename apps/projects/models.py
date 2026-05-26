from django.db import models
from apps.common.models import BaseModel
from apps.accounts.models import User


class Project(BaseModel):

    name = models.CharField(max_length=255)

    description = models.TextField()

    location = models.CharField(max_length=255)

    start_date = models.DateField()

    end_date = models.DateField(null=True, blank=True)

    project_manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        related_name='projects'
    )

    boq = models.FileField(upload_to='boq/')

    def __str__(self):
        return self.name