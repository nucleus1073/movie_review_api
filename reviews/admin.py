from django.contrib import admin

# Register your models here.
from .models import Review, Movie

admin.site.register(Review)  # Registering the Review model
admin.site.register(Movie)  # Registering the Movie model