import django_filters

from .models import Client


class ClientFilter(django_filters.FilterSet):

    class Meta:
        model = Client

        fields = {
            "name": ["exact", "icontains"],
            "email": ["exact", "icontains"],
            "created_at": ["gte", "lte"],
        }