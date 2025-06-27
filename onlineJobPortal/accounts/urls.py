from django.urls import path
from . import views


urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),

    path('register/', views.register, name='register'),
    path('register/user-register/', views.user_register, name='user_register'),
    path('register/admin-register', views.admin_register, name='admin_register'),    
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),

    path('activate/<uidb64>/<token>/', views.activate, name='activate'),
    path('forgot-password/', views.forgotPassword, name='forgotPassword'),
    path('resetpassword-validate/<uidb64>/<token>/', views.resetpassword_validate, name='resetpassword_validate'),
    path('reset-password/', views.resetPassword, name='resetPassword'),
    path('change-password/', views.changePassword, name='changePassword'),
    path('edit-profile/', views.edit_profile, name='edit_profile'),

    path('manage-job/', views.manageJob, name='managejob'),

    # path('my-job/', views.myJob, name='managejob'),


]
