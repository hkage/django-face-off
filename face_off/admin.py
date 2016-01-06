from django.contrib import admin

from face_off.models import UserRepresentation


class UserRepresentationAdmin(admin.ModelAdmin):

    list_display = ('user', 'representative', 'created_at')


admin.site.register(UserRepresentation, UserRepresentationAdmin)
