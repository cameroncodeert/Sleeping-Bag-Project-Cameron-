from django.urls import path
from .views import manage_note

app_name= "Notes"
urlpatterns = [
    path('', manage_note, name='add'),

]
