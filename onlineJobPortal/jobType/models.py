from django.db import models

# Create your models here.

class JobType(models.Model):
    job_type_name = models.CharField(max_length=50, unique=True)
    slug          = models.SlugField(max_length=100, unique=True)
    is_active     = models.BooleanField(default=False)


    def __str__(self):
        return self.job_type_name
