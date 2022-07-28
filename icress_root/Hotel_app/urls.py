from django.urls import path
from.import views

urlpatterns = [
    path('load_room/',views.load_dashboard,name='load_room'),
    path('room_update/<pk>',views.room_update,name='room_update'),
    path('room_delete/<pk>',views.room_delete,name='room_delete'),
]
