from django.urls import path
from track.views import search
urlpatterns = [
    path('', search, name='search')
]