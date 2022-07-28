from django . urls import path
from . import views

app_name='registraion_app'

urlpatterns = [
    path('login/',views.Login,name='login'),
    path('user_login/',views.User_login,name='user_login'),
    path('user_logout/', views.user_logout, name='user_logout'),
    path('userprofile/',views.userprofile,name='userprofile'),
]
