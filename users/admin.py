from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from users.forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ('username', 'name', 'email', 'is_staff', 'is_active',)
    #list_display = ('username', 'name', 'email', 'is_staff', 'is_active',)
    list_filter = ('username', 'is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('username', 'password')}),
        ('Permissions', {'fields': ('is_staff', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('username', 'password1', 'password2', 'is_staff', 'is_active')}
            #'fields': ('username', 'email', 'name', 'password', 'is_staff', 'is_active')}
        ),
    )
    search_fields = ('username',)
    ordering = ('username',)


admin.site.register(CustomUser, CustomUserAdmin)