from django.contrib.auth import get_user_model
from django.db import models
from tickets.models import Ticket

User = get_user_model()


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    ticket = models.ForeignKey(Ticket, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
