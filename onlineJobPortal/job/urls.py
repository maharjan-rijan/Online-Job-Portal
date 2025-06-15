from django.urls import path
from . import views

urlpatterns = [
    path('post-job/', views.postJob, name='postJob'),
    path('job-list/', views.jobList, name='jobList'),
    path('job-detail/', views.jobDetails, name='jobDetail'),
    path('saved-job/', views.saveJob, name='saveJob'),
    path('my-job/', views.myJob, name='myjob'),
    path('edit-job/<int:job_id>', views.editJob, name='editJob'),
    path('delete-job/<int:job_id>/', views.deleteJob, name='deleteJob'),
]
