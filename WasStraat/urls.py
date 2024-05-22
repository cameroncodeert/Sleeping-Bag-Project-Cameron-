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
from django.contrib.auth import views as auth_views
from Employee.views import manageEmployee, dashboard_view, participant_detail





urlpatterns = [
    path('', dashboard_view, name="landing_page"),
    # path('participant/<int:id>/', participant_detail, name='participant_detail'),
    path('participants/', include('Participant.urls', namespace='participants')),
    path('bags/', include('SleepingBag.urls', namespace="bags")),
    path('notes/', include("Notes.urls", namespace="notes")),
    path('location/', include("Location.urls")),
   # path('return_dirty_bag/<int:participant_id>/', views.return_dirty_bag, name='return_dirty_bag'),
    path('admin/', admin.site.urls),
    path('login/', login_user, name="login" ),
    path('register/', register_user, name='register'),
    path('logout/', logout_user, name='logout'),
]
    
