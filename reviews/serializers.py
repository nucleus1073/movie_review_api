from rest_framework import serializers  # Importing Django REST framework's serializer class
from .models import Movie, Review  # Importing Movie and Review models
from django.contrib.auth.models import User  # Importing default Django User model

# Serializer for the User model, handles conversion to/from JSON
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User  # Specify the model to serialize
        fields = ['id', 'email', 'username']  # Specify which fields to include in the serialized output

# Serializer for the Movie model
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie  # Specify the model to serialize
        fields = ['id', 'title', 'release_date', 'genre']  # Include the relevant fields in the serialized output

# Serializer for the Review model
class ReviewSerializer(serializers.ModelSerializer):
    movie = MovieSerializer(read_only=True)  # Nested serializer for movie, read-only
    movie_id = serializers.PrimaryKeyRelatedField(queryset=Movie.objects.all(), write_only=True, source='movie')  # Allow movie to be linked via primary key
    user = serializers.StringRelatedField(read_only=True)  # Read-only field showing the user's string representation
    user_details = UserSerializer(source='user', read_only=True)  # Nested user serializer, read-only

    class Meta:
        model = Review  # Specify the model to serialize
        fields = ['id', 'movie', 'movie_id', 'user', 'user_details', 'review_content', 'rating', 'created_date']  # Fields to include
        read_only_fields = ['user', 'user_details', 'created_date']  # Fields that should be read-only

    # Validation method for the rating field to ensure it's between 1 and 5
    def validate_rating(self, value):
        if not 1 <= value <= 5:  # Check if the rating is within the valid range
            raise serializers.ValidationError("Rating must be between 1 and 5.")  # Raise error if validation fails
        return value  # Return the valid rating

# Serializer for detailed Movie view including related reviews
class MovieDetailSerializer(MovieSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)  # Include related reviews in the detailed view

    class Meta(MovieSerializer.Meta):
        fields = MovieSerializer.Meta.fields + ['reviews']  # Include reviews in the serialized output