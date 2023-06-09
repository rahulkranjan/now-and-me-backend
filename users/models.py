from statistics import mode
from django.db import models
import uuid
from django.db import models, transaction
from django.contrib.auth.models import (
    AbstractBaseUser, PermissionsMixin, BaseUserManager)
from django.utils import timezone

# from vote_module.models import PollingBooth

# Create your models here.


class Role(models.Model):

    IS_SUPERADMIN = 1
    IS_ADMIN = 2
    IS_CLIENT = 3

    ROLE_CHOICES = (
        (IS_SUPERADMIN, 'is_superadmin'),
        (IS_ADMIN, 'is_admin'),
        (IS_CLIENT, 'is_client'),
    )
    ROLES_CHOICES = (
        ('IS_SUPERADMIN', 'is_superadmin'),
        ('IS_ADMIN', 'is_admin'),
        ('IS_CLIENT', 'is_client'),

    )

    id = models.PositiveSmallIntegerField(
        choices=ROLE_CHOICES, primary_key=True)
    name = models.CharField(
        max_length=100, choices=ROLES_CHOICES, blank=True, null=True)

    def __str__(self):
        return str(self.name)


class UserManager(BaseUserManager):

    def _create_user(self, contact, password, **extra_fields):
        if not contact:
            raise ValueError('The given contact must be set')
        try:
            with transaction.atomic():
                user = self.model(contact=contact, **extra_fields)
                user.set_password(password)
                user.save(using=self._db)
                return user
        except:
            raise

    def create_user(self, contact, password=None, **extra_fields):
        extra_fields.setdefault('is_staff', False)
        extra_fields.setdefault('is_superuser', False)
        return self._create_user(contact, password, **extra_fields)

    def create_superuser(self, contact, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('roles_id', 1)

        return self._create_user(contact, password=password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100, blank=True, null=True)
    roles = models.ForeignKey(Role, on_delete=models.CASCADE, default=1)
    contact = models.BigIntegerField(default=0, unique=True)
    avatar = models.FileField(
        upload_to='avtar/', blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    objects = UserManager()

    USERNAME_FIELD = 'contact'

    def save(self, *args, **kwargs):
        super(User, self).save(*args, **kwargs)
        return self

    def __str__(self):
        return str(self.contact)

    class Meta:
        ordering = ['-date_joined']
