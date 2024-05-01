from django.urls import path

from .views import helloNote 

urlpatterns = [
    path('', helloNote, name='helloNote'),
]