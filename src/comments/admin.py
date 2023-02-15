from comments.models import Comment
from django.contrib import admin
from shared.django import TimeStampReadonlyAdmin


@admin.register(Comment)
class CommentAdmin(TimeStampReadonlyAdmin):
    list_display = ["body", "ticket", "user"]
