from .models import JobType

def job_type_links(request):
    job_type_links = JobType.objects.all()
    return dict(job_type_links=job_type_links)