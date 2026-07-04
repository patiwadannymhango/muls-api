from rest_framework import status, viewsets
from rest_framework.permissions import IsAuthenticated,AllowAny
from rest_framework.filters import SearchFilter, OrderingFilter
from .models import Client
from rest_framework.response import Response
from .serializers import ClientSerializer

from django_filters.rest_framework import DjangoFilterBackend

from .filters import ClientFilter


class ClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientSerializer
    queryset = Client.objects.filter(
        is_active=True
    )

    permission_classes = [AllowAny]

    filter_backends = (
        DjangoFilterBackend,
        SearchFilter,
        OrderingFilter,
    )

    filterset_class = ClientFilter

    search_fields = (
        "name",
        "email",
        "phone_number",
    )

    ordering_fields = "__all__"

    ordering = (
        "-created_at",
    )

    # def destroy(self, request, *args, **kwargs):

    #     client = self.get_object()

    #     client.is_active = False

    #     client.save(update_fields=["is_active"])

    #     return Response(
    #         {
    #             "detail": "Client deleted successfully."
    #         },
    #         status=status.HTTP_204_NO_CONTENT,
    #     )