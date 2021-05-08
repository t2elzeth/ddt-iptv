from django.contrib import admin

from . import models


class UserAdmin(admin.ModelAdmin):
    ordering = ('id', 'type')

    list_filter = ('type',)

    readonly_fields = ('id',)


admin.site.register(models.Actor)
admin.site.register(models.Show, UserAdmin)
