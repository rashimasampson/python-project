from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('', include('tvshows_app.urls')),
]
