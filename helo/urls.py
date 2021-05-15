from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from home import views



urlpatterns = [
    path("", views.index, name= 'home'),
  
    path('profile/',views.profile, name= 'profile' ),
    
    path('content_management/',views.content_management, name= 'content_management' ),
    path('demand/',views.demand, name= 'demand' ),
    path('sub/',views.sub, name= 'sub' ),
    path('service/',views.service, name= 'service'), 
    path('provider/',views.provider, name= 'provider'),
    path('add/',views.add, name= 'add'),
    path('view/',views.Service_View, name= 'view'),
    path('notification/',views.notification, name= 'notification'),
    path('driver/',views.driver, name= 'driver'),
    path('add_driver/',views.add_driver, name= 'add_driver'),
    path('location_view/',views.location_view, name= 'location_view'),
    path('map_view/',views.map_view, name= 'map_view'),
    path('agent_view/',views.agent_view, name= 'agent_view'),
    path('charges_view/',views.charges_view, name= 'charges_view'),
]