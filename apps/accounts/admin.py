from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import Group

from . import models


class UserAdmin(BaseUserAdmin):
    ordering = ('is_staff',)

    list_display = ('email',)

    list_filter = ('is_staff',)

    readonly_fields = ('id', 'is_superuser', 'is_staff')
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
    )

    fieldsets = (
        (None, {
            'fields': (
                'id', 'full_name', 'email',
                'is_premium', 'is_superuser', 'is_staff',
            )
        }),
    )


admin.site.register(models.User, UserAdmin)

admin.site.unregister(Group)
