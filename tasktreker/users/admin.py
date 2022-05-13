from django.contrib import admin
from django.contrib.auth import admin as auth_admin
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

from tasktreker.users.forms import UserAdminChangeForm, UserAdminCreationForm

User = get_user_model()


@admin.register(User)
class UserAdmin(auth_admin.UserAdmin):

    form = UserAdminChangeForm
    add_form = UserAdminCreationForm
    fieldsets = (
        (None, {"fields": ("username", "first_name", 'last_name', "password")}),
        (_("Personal info"), {"fields": ('middle_name',  "email")}),
        (
            _("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    'is_client',
                    "is_superuser",
                    'is_admin',
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (_("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    list_display = ["username", "first_name", 'middle_name', 'last_name', 'email', "is_active", "is_staff",
                    'is_client', 'is_admin', "is_superuser"]
    search_fields = ["username", "first_name", 'middle_name', 'last_name', 'email']
