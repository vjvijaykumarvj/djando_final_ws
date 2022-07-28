from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.Home),
    path('register/',include('register_app.urls')),
]
