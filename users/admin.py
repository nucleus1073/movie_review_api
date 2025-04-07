from django.contrib import admin # Importing Django's admin module

# Register your models here.
from django.contrib.auth.admin import UserAdmin as DefaultAdmin  # Importing default UserAdmin from Django for user management
from .models import User, Profile  # Importing custom User and Profile models

# Customizing the Django admin interface for the User model
class UserAdmin(DefaultAdmin):
    list_dislplay = ("email", "username")  # Display email and username fields in the admin list view

admin.site.register(User, UserAdmin)  # Register the custom User model with the Django admin
admin.site.register(Profile)  # Register the Profile model with the Django admin