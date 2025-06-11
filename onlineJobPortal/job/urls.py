from django.urls import path
from . import views


urlpatterns = [
    path('job-list/', views.jobList, name='jobList'),
    path('job-detail/', views.jobDetails, name='jobDetail'),
]
