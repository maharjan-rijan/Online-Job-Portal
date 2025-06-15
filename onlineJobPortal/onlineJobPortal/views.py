from django.shortcuts import render
from job.models import Job
from django.core.paginator import Paginator


def home(request):
    jobs = Job.objects.all().order_by('job_post_date')
    featured_job = Job.objects.all().filter(is_featured = True).order_by('job_post_date')
    paginator = Paginator(jobs, 4)
    featu_page = Paginator(featured_job, 9)
    page = request.GET.get('page')
    paged_jobs = paginator.get_page(page)
    futured_paged = featu_page.get_page(page)
    context = {
        'jobs': paged_jobs,
        'featured_jobs' : futured_paged,

    }
    return render(request, 'home.html', context)

def aboutUs(request):
    context={
        'page_title': 'About Us'
    }
    return render(request, 'about-us.html',context)

def browsecategories(request):
    context={
        'page_title': 'Categories'
    }
    return render(request, 'pages/browse-category.html',context)

def contactUs(request):
    context={
        'page_title': 'Contact Us'
    }
    return render(request, 'contact-us.html',context)