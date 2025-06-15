from django.contrib import admin
from .models import Job

# Register your models here.
class JobAdmin(admin.ModelAdmin):
    list_display = ('job_title','job_slug','job_type','category','is_featured','job_post_date')

admin.site.register(Job, JobAdmin)