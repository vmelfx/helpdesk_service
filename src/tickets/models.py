from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Ticket(models.Model):
    header = models.CharField(max_length=255)
    body = models.TextField()
    customer = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    manager = models.ForeignKey(User, null=True, default=None, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
