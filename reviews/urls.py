from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import MovieViewSet, ReviewViewSet

# Initialize DRF router to manage routes for our ViewSet
router = DefaultRouter()
router.register("movies", MovieViewSet, basename="movie")
router.register("reviews", ReviewViewSet, basename="review")

urlpatterns = router.urls # Include all router-generated routes