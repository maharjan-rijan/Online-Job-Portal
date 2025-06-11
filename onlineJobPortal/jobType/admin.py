from django.contrib import admin
from .models import JobType

# Register your models here.

class JobTypeAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('job_type_name',)}
    list_display = ('job_type_name', 'slug','is_active')

admin.site.register(JobType, JobTypeAdmin)