
from rest_framework import serializers
from .models import Project
from apps.clients.models import Client
from apps.accounts.models import User


class ProjectSerializer(serializers.ModelSerializer):
    client = serializers.PrimaryKeyRelatedField(queryset=Client.objects.all())
    supervisor = serializers.PrimaryKeyRelatedField(
        queryset=User.objects.all(),
        allow_null=True,
        required=False
    )

    client_name = serializers.CharField(source="client.name", read_only=True)
    supervisor_name = serializers.CharField(source="supervisor.get_full_name", read_only=True)

    class Meta:
        model = Project
        fields = [
            "id",
            "name",
            "description",
            "client",
            "client_name",
            "location",
            "start_date",
            "end_date",
            "supervisor",
            "supervisor_name",
            "status",
            "created_at",
            "updated_at",
        ]
        read_only_fields = ["id", "created_at", "updated_at"]