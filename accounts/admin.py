from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import RegistrationRequest, CustomUser


@admin.register(RegistrationRequest)
class RegistrationRequestAdmin(admin.ModelAdmin):
    pass


admin.site.register(CustomUser, UserAdmin)
