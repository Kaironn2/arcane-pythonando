from django.urls import path

from . import views

urlpatterns = [
    path('sign-in/', views.sign_in, name='sign-in'),
    path('login/', views.login, name='login'),
    path('permissions/', views.permissions, name='permissions'),
    path(
        'manager-permission/<int:id>', views.manager_permission,
        name='manager_permission'
    )
]
