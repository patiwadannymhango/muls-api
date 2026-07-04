from django.db import models
from apps.common.models import BaseModel
from apps.accounts.models import User
from apps.projects.models import Project

class Stage(BaseModel):
    
    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        null=False,
        related_name='proejct'
    )
    name = models.CharField(max_length=255)
    description = models.TextField()

    start_date = models.DateField()
    end_date = models.DateField()


    def __str__(self):
        return f"{self.name} "