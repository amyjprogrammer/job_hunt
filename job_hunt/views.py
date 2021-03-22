from django.shortcuts import render

# Create your views here.
"""home page"""
def home(request):
    context = {}
    return render(request, 'job_hunt/home.html', context)
