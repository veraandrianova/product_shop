from django.contrib import admin

from .models import User


@admin.register(User)
class User(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "email")
    search_fields = ("first_name", "last_name", "email")