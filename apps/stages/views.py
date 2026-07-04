from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Stage
from .serializers import StageSerializer

from django_filters.rest_framework import DjangoFilterBackend

from .filters import StageFilter


class StageViewSet(viewsets.ModelViewSet):

    serializer_class = StageSerializer
    queryset = Stage.objects.filter(
        is_active=True
    )

    permission_classes = [AllowAny]

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = StageFilter

    search_fields = (
        "name",
    )

    ordering_fields = "__all__"

    ordering = (
        "-created_at",
    )

