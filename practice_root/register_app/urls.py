from django.urls import path
from.import views

urlpatterns = [
    path('signin/',views.Register),
    path('login/',views.Login),
    path('logout/',views.LogOut),
    path('profile/',views.Profile),
]