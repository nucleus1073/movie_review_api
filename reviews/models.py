from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model  # To import the custom User model dynamically

User = get_user_model()  # Dynamically get the User model

# Movie model to store movie details
class Movie(models.Model):
    title = models.CharField(max_length=25, unique=True)  # Movie title must be unique and can have up to 255 characters
    release_date = models.DateField(null=True, blank=True)  # Optional field for the movie's release date
    genre = models.CharField(max_length=100, null=True, blank=True)  # Optional field for the movie genre

    # Define how the Movie object will be represented as a string (returns title)
    def __str__(self):
        return self.title  # Return the movie title

# Review model to store user reviews for movies
class Review(models.Model):
    movie = models.ForeignKey(Movie, related_name="reviews", on_delete=models.CASCADE)  # Link each review to a specific movie
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link each review to a specific user
    review_content = models.Textfield()  # Store the content of the review as text
    rating = models.PositiveIntegerField()  # Store the review's rating as a positive integer
    created_date = models.DateTimeField(auto_now_add=True)  # Automatically set the review's creation date

    # Define how the Review object will be represented as a string (returns movie title, rating, and user email)
    def __str__(self):
        return f"{self.movie.title} - {self.rating}/5 by {self.user.email}"  # Format the string to display movie, rating, and user