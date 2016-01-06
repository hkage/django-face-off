from django.contrib import admin

from face_off.models import UserRepresentation


class UserRepresentationAdmin(admin.ModelAdmin):
    pass


admin.site.register(UserRepresentation, UserRepresentationAdmin)
