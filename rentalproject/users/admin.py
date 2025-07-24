from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Users


@admin.register(Users)
class UserAdmin(BaseUserAdmin):
    list_display = ('email', 'name', 'role', 'is_staff', 'is_superuser')
    search_fields = ('email', 'name')
    ordering = ('email',)
    list_filter = ('role', 'is_staff', 'is_superuser')

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal Info', {'fields': ('name', 'age', 'bio', 'role')}),
        ('Permissions', {'fields': ('is_active', 'is_staff',
         'is_superuser', 'groups', 'user_permissions')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'name', 'role', 'password1', 'password2'),
        }),
    )
