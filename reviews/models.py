from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Movie(models.Model):
    """
    Movie model represents a film with attributes such as title, release date, and genre.
    Attributes:
        title (str): The title of the movie. Must be unique and can have up to 255 characters.
        release_date (date, optional): The release date of the movie. This field is optional.
        genre (str, optional): The genre of the movie. This field is optional and can have up to 100 characters.
    Methods:
        __str__(): Returns the string representation of the Movie object, which is the movie title.
    """
    title = models.CharField(max_length=255, unique=True)  # Movie title must be unique and can have up to 255 characters
    release_date = models.DateField(null=True, blank=True)  # Optional field for the movie's release date
    genre = models.CharField(max_length=100, null=True, blank=True)  # Optional field for the movie genre

    # Define how the Movie object will be represented as a string (returns title)
    def __str__(self):
        return self.title  # Return the movie title

# Review model to store user reviews for movies
class Review(models.Model):
    """
    Review model represents a user's review for a movie.
    Attributes:
        user (ForeignKey): A foreign key linking the review to a specific user. 
            This establishes a many-to-one relationship with the User model.
        review_content (TextField): The content of the review written by the user.
        rating (PositiveIntegerField): The rating given by the user, stored as a positive integer.
        created_date (DateTimeField): The date and time when the review was created. 
            Automatically set to the current date and time when the review is created.
    Methods:
        __str__(): Returns a string representation of the review, 
            including the movie title, rating, and the user's email.
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link each review to a specific user
    review_content = models.Textfield()  # Store the content of the review as text
    rating = models.PositiveIntegerField()  # Store the review's rating as a positive integer
    created_date = models.DateTimeField(auto_now_add=True)  # Automatically set the review's creation date

    # Define how the Review object will be represented as a string (returns movie title, rating, and user email)
    def __str__(self):
        return f"{self.movie.title} - {self.rating}/5 by {self.user.email}"  # Format the string to display movie, rating, and user