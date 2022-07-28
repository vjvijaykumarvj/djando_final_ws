
from django . urls import path,include
from . import views

urlpatterns = [
    path('student/',views.student_registration),
    path('contact/',views.Contactus),
]