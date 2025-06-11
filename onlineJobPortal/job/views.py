from django.shortcuts import render

# Create your views here.
def jobList(request):
    return render(request, 'job/job-list.html')

def jobDetails(request):
    return render(request, 'job/job-details.html')