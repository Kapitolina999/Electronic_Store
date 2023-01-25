from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext_lazy

User = get_user_model()


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    # fields = ("first_name", "last_name", "email", "company")
    fieldsets = (
        (None, {"fields": ("username", "password")}),
        (gettext_lazy("Personal info"), {"fields": ("first_name", "last_name", "email", "company")}),
        (
            gettext_lazy("Permissions"),
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
            },
        ),
        (gettext_lazy("Important dates"), {"fields": ("last_login", "date_joined")}),
    )
    add_fieldsets = (
        (
            None,
            {
                "classes": ("wide",),
                "fields": ("username", "password1", "password2", 'company'),
            },
        ),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'company', )
    list_filter = ('is_active', 'company')
    exclude = ('password', )
    readonly_fields = ('last_login', 'date_joined', )





