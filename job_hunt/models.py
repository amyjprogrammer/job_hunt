from django.db import models
import datetime

# Create your models here.
class JobHunt(models.Model):
    company_name = models.CharField(max_length=200)
    date_applied = models.DateField(help_text = 'Please use the following format: <em>YYYY-MM-DD</em>')
    applied_how = [
        ('Indeed', 'Indeed'),
        ('LinkedIn', 'LinkedIn'),
        ('Company_website', 'Company website'),
    ]
    applied_on = models.CharField(max_length=20, choices=applied_how, default='Company_website')
    reject_email = models.BooleanField(default=False)
    interview = models.BooleanField(default=False)
    role = models.CharField(max_length=200)
    notes = models.TextField(blank=True, null=True)
