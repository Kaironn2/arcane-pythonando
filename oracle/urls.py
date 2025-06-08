from django.urls import path

from . import views

urlpatterns = [
    path('ai-trainning/', views.ai_trainning, name='ai_trainning'),
    path('chat/', views.chat, name='chat'),
    path('stream-response/', views.stream_response, name='stream_response'),
    path('info-source/<int:id>/', views.info_source, name='info_source'),
]
