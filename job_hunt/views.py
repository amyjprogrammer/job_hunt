from django.shortcuts import render, get_object_or_404, redirect

from .models import JobHunt
from .forms import JobHuntForm

# Create your views here.
"""home page"""
def home(request):
    job_hunt = JobHunt.objects.all()
    context = {'job_hunt': job_hunt}
    return render(request, 'job_hunt/home.html', context)

def add_job_hunt(request):
    """adding a new entry"""
    if request.method != "POST":
        #show blank form
        form = JobHuntForm()
    else:
        #entering new data
        form = JobHuntForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('job_hunt:home')

    context = {'form': form}
    return render(request, 'job_hunt/add_job_hunt.html', context)

def edit_job_hunt(request, hunt_id):
    """Editing your job post"""
    job_hunting = get_object_or_404(JobHunt, id=hunt_id)

    if request.method != "POST":
        #show previous info
        edit_form = JobHuntForm(instance=job_hunting)

    else:
        edit_form = JobHuntForm(request.POST, instance=job_hunting)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('job_hunt:home')

    context = {'edit_form': edit_form, 'job_hunting': job_hunting}
    return render(request, 'job_hunt/edit_job_hunt.html', context)

def delete_job(request, job_id):
    """Deleting Job"""
    job_hunt = get_object_or_404(JobHunt, id=job_id)

    if request.method == "POST":
        job_hunt.delete()
        context={'job_hunt': job_hunt}
        return redirect('job_hunt:home')
