"""Model definitions for the django-face-off application."""

from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class UserRepresentation(models.Model):

    user = models.ForeignKey(AUTH_USER_MODEL, related_name='represented_users')
    representative = models.ForeignKey(AUTH_USER_MODEL, related_name='representatives')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _(u'User representative')
        verbose_name_plural = _(u'User representatives')

    def __unicode__(self):
        return '{} -> {}'.format(self.representative, self.user)
