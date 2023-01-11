from django.contrib import admin
from .models import Public_pitches, Tweet, Resume, Job, JobPosting, JobApplication
# Register your models here.

admin.site.register(Public_pitches)
admin.site.register(Tweet)
admin.site.register(Resume)

admin.site.register(Job)
admin.site.register(JobPosting)
admin.site.register(JobApplication)
