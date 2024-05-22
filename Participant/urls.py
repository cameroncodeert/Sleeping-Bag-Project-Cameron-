from django.urls import path
from .views import participant_detail, remove_participant, add_participant

app_name = "participants"
urlpatterns = [

    path('<int:id>/', participant_detail, name='participant_details'),
    #/partcipants/<int:id>
    path('delete/<int:participant_id>',  remove_participant, name='remove_participant'),
    path('add/', add_participant, name='add_participant'),

    ]
    
