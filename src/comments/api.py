from comments.models import Comment
from comments.serializers import CommentSerializer
from django.http import JsonResponse
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ViewSet
from shared.permissions import PermissionsMixin
from shared.serializers import ResponseMultiSerializer, ResponseSerializer
from tickets.permissions import IsOwner, RoleIsAdmin, RoleIsManager, RoleIsUser


class CommentsAPISet(PermissionsMixin, ViewSet, GenericViewSet):
    lookup_field = "ticket_id"
    lookup_url_kwarg = "comment_id"

    ticket_id: int = lookup_field
    comment_id: int = lookup_url_kwarg

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
        return Comment.objects.filter(ticket_id=self.ticket_id).order_by("-created_at")

    def list(self, request, ticket_id):
        queryset = self.get_queryset()
        serializer = CommentSerializer(queryset, many=True)
        response = ResponseMultiSerializer({"results": serializer.data})

        return Response(response.data)

    def retrieve(self, request, ticket_id, comment_id):
        instance = Comment.objects.filter(ticket_id=ticket_id).get(id=comment_id)
        serializer = CommentSerializer(instance)
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
        instance = Comment.objects.filter(ticket_id=ticket_id).get(id=comment_id)

        context: dict = {
            "request": self.request,
        }
        serializer = CommentSerializer(instance, data=request.data, context=context)
        serializer.is_valid()
        serializer.save()

        response = ResponseSerializer({"result": serializer.data})

        return JsonResponse(response.data)

    def destroy(self, request, ticket_id, comment_id):
        instance = Comment.objects.filter(ticket_id=ticket_id).get(id=comment_id)
        instance.delete()

        return JsonResponse({}, status=status.HTTP_204_NO_CONTENT)
