from django.contrib import admin

from account.models import Profile


# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """Profile model admin settings."""

    list_display = ["user", "date_of_birth", "photo"]
    raw_id_fields = ["user"]
