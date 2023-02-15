from comments.models import Comment
from rest_framework import serializers
from tickets.models import Ticket


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = "__all__"
        read_only_fields = ["ticket", "user", "prev_comment"]

    def validate(self, attrs):
        request = self.context["request"]
        ticket_id: int = request.parser_context["kwargs"]["ticket_id"]
        ticket: Ticket = Ticket.objects.get(id=ticket_id)

        last_comment: Comment | None = ticket.comments.last()

        attrs["ticket"] = ticket
        attrs["user"] = request.user
        attrs["prev_comment"] = last_comment

        return attrs


class CommentRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["id", "created_at", "updated_at", "user", "ticket", "prev_comment"]
        read_only_fields = ["ticket", "user", "prev_comment"]
