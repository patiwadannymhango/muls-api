from django.contrib import admin

from .models import Client


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "email",
        "phone_number",
        "created_at",
    )

    search_fields = (
        "name",
        "email",
    )

    ordering = (
        "-created_at",
    )