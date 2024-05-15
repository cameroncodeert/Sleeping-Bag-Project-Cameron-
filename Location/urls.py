# URL patterns for the Location app

from django.urls import path
# from . import views
from .views import manageLocation

urlpatterns = [
    path('', manageLocation, name='manageLocation'),  
    # Route for managing locations, linked to manageLocation view

]
