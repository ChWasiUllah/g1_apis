from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from core.models import User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    permission_classes = ['GET', 'POST', 'PUT', 'PATCH', 'DELETE']
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("password1", "password2", 'email', 'full_name'),
            },
        ),
    )
    ordering = ('email',)