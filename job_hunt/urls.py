from django.urls import path

from . import views

app_name = 'job_hunt'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_job_hunt/', views.add_job_hunt, name='add_job_hunt'),
    path('edit-job/<int:hunt_id>/', views.edit_job_hunt, name='edit_job_hunt'),
]
