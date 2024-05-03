from django.urls import path
# from . import views
from .views import manageLocation
# urlpatterns = [
#     #/location
#     path('', hello)
#     #/location/add
# ]

# from django.urls import path
# from .views import hello  # Make sure to import the hello view

urlpatterns = [
    path('', manageLocation, name='manageLocation'),  # Maps /hello/ to the hello view
]
