from enum import Enum

__all__ = ["Role"]


class Role(Enum):
    ADMIN = "admin"
    MANAGER = "manager"
    USER = "user"
