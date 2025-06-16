from django.db import models
from django.urls import reverse

from accounts.models import Account
from category.models import Category
from jobType.models import JobType

# Create your models here.
class Job(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    job_title = models.CharField(max_length=255)
    job_slug = models.SlugField(max_length=100, unique=True)
    job_type = models.ForeignKey(JobType, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True)
    application_deadline = models.DateField(null=True)
    salary = models.CharField(max_length=100, blank=True)
    job_description = models.TextField()
    job_requirements = models.TextField()
    company_name = models.CharField(max_length=255)
    company_website = models.CharField(max_length=255)
    company_location = models.CharField(max_length=255)

    is_featured = models.BooleanField(default=False)
    job_post_date = models.DateTimeField(null=True)

    def get_url(self):
        return reverse('jobDetail',args=[self.category.slug, self.job_slug])

    def __str__(self):
        return self.job_title

