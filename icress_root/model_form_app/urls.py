
from django . urls import path
from . import views
app_name='modelforms_app'

urlpatterns = [
    path('model_form/',views.Model_Form),
    path('emp_Update/<pk>',views.Emp_Update,name='emp_Update'),
    path('emp_Delete/<pk>',views.Emp_Delete,name='emp_Delete'),
]