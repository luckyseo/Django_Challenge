from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class CustomUserAdmin(UserAdmin):
    """
    ModelAdmin: create admin panel 
    Controls User / on websit and it shows "Users" instead of "User"
    list_display =[column value for useradmin panal]
    list_filter[]
    search_fields=["col_val__startswith"]
    """
    fieldsets = (
        (
            "Profile",
            {
                "fields": ("username", "password", "name", "email", "is_host"),
                "classes": ("wide",),
            },
        ),
        (
            "Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes": ("collapse",),
            },
        ),
        (
            "Important Dates",
            {
                "fields": ("last_login", "date_joined"),
                "classes": ("collapse",),
            },
        ),
    )

    list_display=(
        "username","email","name","is_host"
    )
    pass