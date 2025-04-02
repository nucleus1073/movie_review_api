from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets  # Importing DRF's viewsets to simplify API views
from rest_framework.permissions import IsAuthenticated  # Importing permission class to ensure authentication
from .models import Movie, Review  # Importing Movie and Review models
from .serializers import MovieSerializer, MovieDetailSerializer, ReviewSerializer  # Importing serializers for models
from .permissions import IsAuthorOrReadOnly  # Custom permission for review authors
from django_filters.rest_framework import DjangoFilterBackend  # Importing Django filter backend for filtering
from rest_framework.filters import SearchFilter, OrderingFilter  # Importing filters for search and ordering

# ViewSet for handling movie-related operations
class MovieViewSet(viewsets.ModelViewSet):
    queryset = Movie.objects.all()  # Retrieve all movies from the database
    serializer_class = MovieSerializer  # Use MovieSerializer by default
    permission_classes = [IsAuthenticated]  # Require authentication for all actions
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Enable filtering, searching, and ordering
    filterset_fields = ['title']  # Allow filtering by movie title
    search_fields = ['title']  # Allow searching by movie title

    # Use a different serializer for detailed movie views
    def get_serializer_class(self):
        if self.action == 'retrieve':  # If retrieving a single movie
            return MovieDetailSerializer  # Use the detailed serializer
        return MovieSerializer  # Use the default serializer otherwise

# ViewSet for handling review-related operations
class ReviewViewSet(viewsets.ModelViewSet):
    queryset = Review.objects.all()  # Retrieve all reviews from the database
    serializer_class = ReviewSerializer  # Use ReviewSerializer by default
    permission_classes = [IsAuthenticated]  # Require authentication for all actions
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]  # Enable filtering, searching, and ordering
    search_fields = ['rating']  # Allow searching reviews by rating
    ordering_fields = ['rating']  # Allow ordering reviews by rating

    # Overriding here to save the user making the request as the author of the review
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # Set the user before saving the review