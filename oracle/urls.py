from django.urls import path

from . import views

urlpatterns = [
    path('ai_trainning/', views.ai_trainning, name='ai_trainning'),
    path('chat/', views.chat, name='chat')
]
