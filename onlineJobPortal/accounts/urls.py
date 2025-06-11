from django.urls import path
from . import views


urlpatterns = [
    path('register/', views.register, name='register'),
    path('register/user-register/', views.user_register, name='user_register'),
    path('register/admin-register', views.admin_register, name='admin_register'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
]
