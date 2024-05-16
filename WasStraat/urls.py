"""
URL configuration for WasStraat project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
# from django.contrib.auth.views import LoginView
from .views import landing_page, login_user, register_user, logout_user
from SleepingBag.views import swap_sleeping_bag, success_view, report_lost_bag #return_dirty_bag
from Participant.views import dashboard_view, participant_detail
from django.contrib.auth import views as auth_views
from Employee.views import manageEmployee, dashboard_view, participant_detail
from Participant.views import add_participant, remove_participant

    

urlpatterns = [
    path('', dashboard_view, name="landing_page"),
    path('add_participant/', add_participant, name='add_participant'),
    path('participant/<int:id>/', participant_detail, name='participant_detail'),
    path('remove_participant/<int:participant_id>/', remove_participant, name='remove_participant'),
    path('manage_employee/', manageEmployee, name='manage_employee'),
    path('swap_bag/<int:participant_id>/', swap_sleeping_bag, name='swap_bag'),
    path('report_lost_bag/<int:bag_id>/', report_lost_bag, name='report_lost_bag'),
   # path('return_dirty_bag/<int:participant_id>/', views.return_dirty_bag, name='return_dirty_bag'),
    path('success/', success_view, name='success'),
    path('admin/', admin.site.urls),
    path('location/', include("Location.urls")),
    path('note/', include("Notes.urls")),
    path('login/', login_user, name="login" ),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
]
    
