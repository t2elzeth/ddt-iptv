import django_filters

from django.contrib.auth import get_user_model

User = get_user_model()


class UserFilter(django_filters.rest_framework.FilterSet):
    full_name = django_filters.CharFilter(lookup_expr="icontains")
    email = django_filters.CharFilter(lookup_expr="icontains")
    age = django_filters.CharFilter()
    city = django_filters.CharFilter(lookup_expr="icontains")
    marrital_status = django_filters.CharFilter()
    sex = django_filters.CharFilter()
    religion = django_filters.CharFilter(lookup_expr="icontains")

    class Meta:
        model = User
        fields = ["full_name", "email", "age", "city", "marrital_status", "sex", "religion"]
