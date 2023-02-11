from tickets.models import Ticket
from users.models import Role, User


class PermissionsMixin:
    def _get_tickets(self):
        """
        Get all own tickets for managers and all tickets for admins
        """
        user: User = self.request.user

        if user.role == Role.ADMIN:
            return Ticket.objects.all()
        elif user.role == Role.MANAGER:
            return Ticket.objects.filter(manager=user)

        return Ticket.objects.filter(customer=user)
