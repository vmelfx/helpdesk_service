from comments.models import Comment
from comments.serializers import CommentSerializer
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from shared.permissions import PermissionsMixin
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.models import Ticket
from tickets.permissions import IsOwner, RoleIsAdmin, RoleIsManager, RoleIsUser


class CommentsAPISet(PermissionsMixin, ViewSet, GenericViewSet):
    lookup_field = "ticket_id"
    lookup_url_kwarg = "comment_id"

    def get_permissions(self):
        if self.action == "list":
            permission_classes = [RoleIsAdmin | RoleIsManager | RoleIsUser]
        elif self.action == "create":
            permission_classes = [RoleIsUser | RoleIsManager]
        elif self.action == "retrieve":
            permission_classes = [IsOwner | RoleIsAdmin | RoleIsManager]
        elif self.action == "update":
            permission_classes = [RoleIsUser | RoleIsManager | RoleIsAdmin]
        elif self.action == "destroy":
            permission_classes = [RoleIsAdmin | RoleIsManager]
        else:
            permission_classes = []

        return [permission() for permission in permission_classes]

    def get_queryset(self):
        tickets = self._get_tickets()
        ticket = get_object_or_404(tickets, id=self.kwargs[self.lookup_field])
        comments = ticket.comments.order_by("-created_at")
        return comments

    def list(self, request, ticket_id):
        queryset = self.get_queryset()
        serializer = CommentSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return Response(response.data)

    def retrieve(self, request, ticket_id, comment_id):
        ticket = get_object_or_404(Ticket.objects.filter(customer=request.user.id), id=ticket_id)
        comment = get_object_or_404(ticket.comments, id=comment_id)
        serializer = CommentSerializer(comment)
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def create(self, request, ticket_id):
        context: dict = {
            "request": self.request,
        }
        serializer = CommentSerializer(data=request.data, context=context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data, status=status.HTTP_201_CREATED)

    def update(self, request, ticket_id, comment_id):
        ticket = get_object_or_404(Ticket.objects.filter(customer=request.user.id), id=ticket_id)
        comment = get_object_or_404(ticket.comments, id=comment_id)

        context: dict = {
            "request": self.request,
        }
        serializer = CommentSerializer(comment, data=request.data, context=context)
        serializer.is_valid()
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, ticket_id, comment_id):
        comment = Comment.objects.filter(ticket_id=ticket_id).get(id=comment_id)
        comment.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
