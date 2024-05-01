from django.urls import path
# from . import views
from .views import hello
# urlpatterns = [
#     #/location
#     path('', hello)
#     #/location/add
# ]

# from django.urls import path
# from .views import hello  # Make sure to import the hello view

urlpatterns = [
    path('', hello, name='hello'),  # Maps /hello/ to the hello view
]
