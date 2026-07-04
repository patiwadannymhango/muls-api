
from rest_framework import serializers
from .models import Project
from apps.Project.models import Project



class ProjectSerializer(serializers.ModelSerializer):
    project = serializers.PrimaryKeyRelatedField(queryset=Project.objects.all())
    project_name = serializers.CharField(source="Project.name", read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "project",
            "project_name",            
            "start_date",
            "end_date",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]