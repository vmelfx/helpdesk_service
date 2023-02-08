from tickets.models import Ticket
from users.schemas import Role


class PermissionsMixin:
    def _get_tickets(self):
        """
        Get all own tickets for managers and all tickets for admins
        """
        role: Role = self.request.user.role

        if role == Role.ADMIN:
            return Ticket.objects.all()
        elif role == Role.MANAGER:
            return Ticket.objects.filter(manager=self.request.user)

        return Ticket.objects.filter(customer=self.request.user)
