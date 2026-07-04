import django_filters

from .models import Stage


class StageFilter(django_filters.FilterSet):

    class Meta:
        model = Stage

        fields = {
            "name": ["exact", "icontains"],
            "created_at": ["gte", "lte"],
        }