from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.validators import ASCIIUsernameValidator
from django.contrib.postgres.fields import CICharField, CIEmailField
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from users.managers import UserManager


class User(AbstractBaseUser):
    username_validator = ASCIIUsernameValidator

    id = models.AutoField(primary_key=True)
    username = CICharField(
        _("username"),
        max_length=150,
        unique=True,
        help_text=_("Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only."),
        validators=[username_validator],
        error_messages={
            "unique": _("A user with that username already exists."),
        },
    )
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)
    email = CIEmailField(
        _("email address"), unique=True, error_messages={"unique": _("A user with that email address already exists")}
    )
    is_active = models.BooleanField(
        _("active"),
        default=True,
        help_text=_("Designates whether this user should be treated as active. Unselect this instead of del"),
    )
    is_staff = models.BooleanField(
        _("staff status"),
        default=False,
        help_text=_("Designates whether the user can log into this admin site."),
    )
    last_login = models.DateTimeField(
        _("last login"), help_text=_("Show the last login date and time"), default=timezone.now
    )
    date_joined = models.DateTimeField(_("date joined"), default=timezone.now)

    role = models.CharField(_("role"), max_length=7, help_text=_("Designates user role in the system"), choices=[])

    objects = UserManager()

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)

    def get_full_name(self):
        """
        Return the first_name plus the last_name, with a space in between.
        """
        full_name = "%s %s" % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        """Return the short name for the user."""
        return self.first_name

    EMAIL_FIELD = "email"
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
