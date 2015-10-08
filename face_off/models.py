
from django.db import models
from django.utils.translation import ugettext_lazy as _

try:
    from django.contrib.auth import get_user_model
    User = get_user_model()
except ImportError:
    from django.contrib.auth.models import User


class UserRepresentation(models.Model):

    user = models.ForeignKey(User, related_name='represented_users')
    representative = models.ForeignKey(User, related_name='representatives')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _(u'User representative')
        verbose_name_plural = _(u'User representatives')
