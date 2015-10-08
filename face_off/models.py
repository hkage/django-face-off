from django.contrib.auth import get_user_model
from django.db import models
from django.utils.translation import ugettext_lazy as _


class UserRepresentation(models.Model):

    user = models.ForeignKey(get_user_model())
    representative = models.ForeignKey(get_user_model())
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = _(u'User representative')
        verbose_name_plural = _(u'User representatives')
