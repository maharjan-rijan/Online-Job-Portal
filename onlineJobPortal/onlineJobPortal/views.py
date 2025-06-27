from django.shortcuts import render
from job.models import Job
from django.core.paginator import Paginator
from django.db.models import Q

def home(request):
    jobs = Job.objects.all().order_by('job_post_date')
    featured_jobs = Job.objects.filter(is_featured=True).order_by('job_post_date')

    paginator = Paginator(jobs, 4)
    page = request.GET.get('page')
    paged_jobs = paginator.get_page(page)

    featured_paginator = Paginator(featured_jobs, 9)
    featured_page = request.GET.get('featured_jobs_page')
    featured_paged_jobs = featured_paginator.get_page(featured_page)
    context = {
        'jobs': paged_jobs,
        'featured_paged_jobs':featured_paged_jobs
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

def search(request):
    if ('keyword' in request.GET) | ('location' in request.GET):
        keyword = request.GET['keyword']
        location = request.GET['location']
        if keyword or location:
            jobs = Job.objects.order_by('job_post_date').filter(Q(job_description__icontains=keyword)|Q(job_title__icontains=keyword)|Q(company_location=location))
    context={
        'jobs':jobs,
        'page_title': 'Job List'
    }
    return render(request, 'job/job-list.html', context)