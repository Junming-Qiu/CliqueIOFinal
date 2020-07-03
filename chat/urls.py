from django.urls import path

from . import views

urlpatterns = [
    path('', views.main_chat_room, name='main_chat_room'),
    path('<str:room_name>/', views.room, name='room'),
    #path('start_chat/<int:applicant_id>/<int:user_id>/', views.start_chat, name = 'start_chat'),
]