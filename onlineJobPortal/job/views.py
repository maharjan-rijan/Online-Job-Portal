from django.shortcuts import render, get_object_or_404,redirect

from category.models import Category
from django.core.paginator import Paginator
from .form import JobForm
from .models import Job


# Create your views here.
def postJob(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job = form.save(commit=False)
            job.user = request.user
            job.save()
            return redirect('jobList')
    else:
        form= JobForm()
    context = {
        'form': form,
        'page_title': 'Post Job'
    }
    
    return render(request, 'job/post-job.html',context)

def jobList(request, category_slug=None):
    categories = None
    jobs = None
    if category_slug != None:
        categories = get_object_or_404(Category, slug=category_slug)
        jobs = Job.objects.filter(category=categories)
        paginator = Paginator(jobs, 1)
        page = request.GET.get('page')
        paged_jobs = paginator.get_page(page)
    else:
        jobs = Job.objects.all().order_by('id')
        paginator = Paginator(jobs, 4)
        page = request.GET.get('page')
        paged_jobs = paginator.get_page(page)
    context = {
        'jobs': paged_jobs,
        'page_title': 'Job List'
    }
    return render(request, 'job/job-list.html',context)

def jobDetails(request):
    context = {
        'page_title': 'Job Detail'
    }
    return render(request, 'job/job-details.html',context)

def saveJob(request):
    context = {
        'page_title': 'Save Job'
    }
    return render(request,'job/saved-job.html',context)

def myJob(request):
    user = request.user
    jobs = Job.objects.filter(user=user) 
    context = {
        'my_job': jobs,
        'page_title': 'Save Job'
    }
    return render(request,'job/manage-job.html',context)
