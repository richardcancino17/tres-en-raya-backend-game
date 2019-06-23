from django.db.models import *
from django.db import models
from django.contrib.auth.models import PermissionsMixin, BaseUserManager, \
    AbstractBaseUser
from django.contrib.auth.validators import ASCIIUsernameValidator, \
    UnicodeUsernameValidator
from django.utils import six
from django.utils.translation import ugettext_lazy as _


class UserManager(BaseUserManager):
    def _create_user(self, email, password, is_staff,
                     is_superuser, **extra_fields):
        user = self.model(email=email, is_active=True,
                          is_staff=is_staff, is_superuser=is_superuser,
                          **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, username, password=None, **extra_fields):
        return self._create_user(email, password, False, False,
                                 **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self._create_user(email, password, True, True, **extra_fields)


class Player(AbstractBaseUser, PermissionsMixin):
    objects = UserManager()
    is_staff = models.BooleanField(default=False)

    email = models.EmailField(unique=True)
    username_validator = UnicodeUsernameValidator() \
        if six.PY3 else ASCIIUsernameValidator()
    username = models.CharField(_('username'),
                                max_length=150, unique=True,
                                validators=[username_validator],
                                help_text=_('Required. 150 characters '
                                            'or fewer. Letters, digits and '
                                            '@/./+/-/_ only.'),
                                error_messages={
                                    'unique':
                                        _("A player with this "
                                          "username already exists."), })

    is_active = models.BooleanField(default=True)
    created_at = models.DateField(auto_now_add=True)
    update_at = models.DateField(auto_now=True)

    USERNAME_FIELD = 'email'

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = "Player"
        verbose_name_plural = "Players"

    def save(self, force_insert=False, force_update=False, *args, **kwargs):
        if not self.username:
            username = ('%s' % (
                self.email.split('@')[0])).lower()
            incidences = Player.objects.filter(
                username__icontains=username
            ).count()
            if incidences > 0:
                username = '{username}{incidences}'.format(
                    username=username,
                    incidences=incidences
                )
            self.username = username
        super(Player, self).save(*args, **kwargs)
