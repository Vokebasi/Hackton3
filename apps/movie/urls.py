from django.db import router
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import FilmViewSet, FavoriteView

router = DefaultRouter()

router.register('film', FilmViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('saved/', FavoriteView.as_view())
    
]

