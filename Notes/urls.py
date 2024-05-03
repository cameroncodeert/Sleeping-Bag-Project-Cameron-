from django.urls import path
from .views import manage_note

urlpatterns = [
    path('', manage_note, name='manageNote'),
]
