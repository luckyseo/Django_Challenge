from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User
# Register your models here.

@admin.register(User)
class userAdmin(UserAdmin):
    fieldsets=(
        (   
            "Profile",
            {
                "fields": (
                    "first_name",
                    "last_name",
                ),
            },
        ),
        ("Permissions",
            {
                "fields": (
                    "is_active",
                    "is_staff",
                    "is_superuser",
                    "groups",
                    "user_permissions",
                ),
                "classes":("collapse",),
            },
        ),
        ("Important dates", 
         {"fields": ("last_login", "date_joined")}),

    )
    list_display =("username","first_name","last_name","email")