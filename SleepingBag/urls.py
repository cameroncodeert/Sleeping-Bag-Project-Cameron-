from django.urls import path
from .views import swap_sleeping_bag, report_lost_bag, wash_now, update_bag, stock

app_name = "bags"

urlpatterns = [
    path('update_bag/<int:bag_id>/', update_bag, name='update'),
    path('swap_bag/<int:participant_id>/', swap_sleeping_bag, name='swap_bag'),
    path('report_lost_bag/<int:bag_id>/', report_lost_bag, name='report_lost_bag'),
    path('wash_now/<int:bag_id>/', wash_now, name='wash_now'),
    path('stock/<int:location_id>/', stock, name='stock'), 


    ]

