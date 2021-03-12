from rest_framework import viewsets, mixins
from rest_framework.decorators import action

from . import serializers, models, filters


class ShowViewSet(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  viewsets.GenericViewSet):

    serializer_class = serializers.ShowSerializer
    queryset = models.Show.objects.all()
    filterset_class = filters.ShowsFilter

    def filter_queryset(self, queryset):
        if self.action == "last":
            queryset = super().filter_queryset(queryset.order_by('-id'))
            return queryset[:10]
        return super().filter_queryset(queryset)

    @action(methods=['get'], detail=False)
    def last(self, request):
        return self.list(request)
