from django.db import models
from apps.common.models import BaseModel
from apps.projects.models import Project


class Material(BaseModel):

    class Unit(models.TextChoices):
        PCS = 'PCS', 'Pieces'
        BAGS = 'BAGS', 'Bags'
        TONS = 'TONS', 'Tons'
        LITERS = 'LITERS', 'Liters'

    project = models.ForeignKey(
        Project,
        on_delete=models.CASCADE,
        related_name='materials'
    )

    name = models.CharField(max_length=255)

    unit = models.CharField(
        max_length=20,
        choices=Unit.choices
    )

    quantity = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        default=0
    )

    def __str__(self):
        return self.name