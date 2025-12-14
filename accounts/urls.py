from django.urls import path
from . import views



urlpatterns = [
    path("login/", views.manual_login, name='manual_login'),

    path('logout/',views.manual_logout,name = 'manual_logout'),
    path('signup/',views.manual_signup, name='manual_signup'),

   
 
]