"""Model definitions for the django-face-off application."""

import six
from django.conf import settings
from django.db import models
from django.utils.translation import ugettext_lazy as _


AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


class UserRepresentation(models.Model):

    user = models.ForeignKey(AUTH_USER_MODEL, unique=True, 
                             related_name='represented_users', 
                             on_delete=models.CASCADE)
    representative = models.ForeignKey(AUTH_USER_MODEL, unique=True, 
                                       related_name='representatives',
                                       on_delete=models.CASCADE)
    redirect_to = models.CharField(max_length=200, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        permissions = (
            ('can_support', _(u'Can support users by switching perspective')),
        )
        verbose_name = _(u'User representative')
        verbose_name_plural = _(u'User representatives')

    @six.python_2_unicode_compatible
    def __unicode__(self):
        return '{} -> {}'.format(self.representative, self.user)
