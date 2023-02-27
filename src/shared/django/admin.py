from typing import Tuple

from django.contrib.admin import ModelAdmin

_FIELDS = ("created_at", "updated_at")


class TimeStampReadonlyAdmin(ModelAdmin):
    readonly_fields = _FIELDS
    list_display: Tuple = _FIELDS
    list_filter: Tuple = _FIELDS
    search_fields = _FIELDS
