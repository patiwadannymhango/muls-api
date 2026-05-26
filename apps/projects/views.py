from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import Project
from .serializers import ProjectSerializer


class ProjectViewSet(viewsets.ModelViewSet):

    queryset = Project.objects.select_related(
        'project_manager'
    ).all()

    serializer_class = ProjectSerializer

    permission_classes = [IsAuthenticated]

    search_fields = ['name', 'location']

    ordering_fields = ['created_at']