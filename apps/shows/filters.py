import django_filters

from . import models


class ShowsFilter(django_filters.rest_framework.FilterSet):
    title = django_filters.CharFilter(lookup_expr="icontains")
    type = django_filters.CharFilter(lookup_expr="iexact")
    genre = django_filters.CharFilter(lookup_expr="iexact")

    class Meta:
        model = models.Show
        fields = ["title", "type", "genre"]
