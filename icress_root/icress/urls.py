
from django.contrib import admin
from django.urls import path,include
from.import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/',views.home),
    path('courses/',include('courses.urls')),
    path('contactus/',views.contact),
    path('aboutus/',views.about_us),
    path('registermp/',views.employee_registration),
    path('studenthp/',include('reg_app.urls')),
    path('login_logout/',views.login_logout),
    path('dtl/',views.dtl),
    path('employee/',include('employee_register_app.urls')),
    path('studentDJF/',include('student_form_app.urls')),
    path('modelformcreate/',include('model_form_app.urls')),
    path('registersign/',include('login_registration_app.urls')),
    path('vijay/',include('VIJAY_app.urls')),
    path('Hotel/',include('Hotel_app.urls'))
]
