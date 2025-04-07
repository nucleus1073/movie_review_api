from django.db import models   # Importing Django's ORM (Object-Relational Mapping) system

# Create your models here. 
from django.contrib.auth.models import AbstractUser, BaseUserManager  # Importing base classes for custom user models and managers

# Custom manager for User model to handle user creation logic
class UserManager(BaseUserManager):
    # Method to create a standard user with an email and password
    def create_user(self, email, password):
        if not email:  # Check if email is provided, raise an error if not
            raise ValueError("Email is required")
        user = self.model(email=self.normalize_email(email))  # Normalize email and create a user instance
        user.set_password(password)  # Hash the password before storing it
        user.save(using=self._db)  # Save the user to the database
        return user  # Return the created user
    
    # Method to create a superuser (admin) with elevated permissions
    def create_superuser(self, email, password):
        user = self.create_user(email=email, password=password)  # Create a standard user first
        user.is_staff = True  # Grant staff privileges
        user.is_superuser = True  # Grant superuser privileges (admin access)
        user.save(using=self._db)  # Save the updated user to the database
        return user  # Return the created superuser

# Custom User model inheriting from Django's built-in AbstractUser
class User(AbstractUser):
    email = models.EmailField(unique=True, max_length=255)  # Use email as a unique identifier
    username = models.CharField(unique=False, max_length=15)  # Username is not unique (email serves as unique field)
    objects = UserManager()  # Assign the custom user manager to this model
    USERNAME_FIELD = 'email'  # Use email instead of username for login
    REQUIRED_FIELDS = []  # No additional required fields

# Profile model extending the user with additional attributes
class Profile(models.Model):
    pic = models.URLField()  # URL for the profile picture, typically stored in object storage (e.g., AWS S3)
    address = models.CharField(max_length=100)  # User's address with a character limit of 100
    country = models.CharField(max_length=50)  # User's country with a character limit of 50
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)  # One-to-one link with the User model, allowing for optional association