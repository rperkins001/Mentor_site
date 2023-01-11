from django.db import models
import uuid
from django.db.models.deletion import CASCADE
from users.models import Profile


class Public_pitches(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField()
    members = models.PositiveIntegerField()
        
class Tweet(models.Model):
    text = models.CharField(max_length=280)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
class Resume(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True)
    resume = models.FileField(upload_to='resumes/')
    
    def __str__(self):
        return str(self.resume)
    
class Job(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.title)

class JobPosting(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField()
    location = models.CharField(max_length=50)
    
    def __str__(self):
        return str(self.title)

class JobApplication(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField()
    resume = models.FileField(upload_to='resumes/')
    cover_letter = models.TextField()
    job = models.ForeignKey(JobPosting, on_delete=models.CASCADE)
    
    def __str__(self):
        return str(self.last_name, self.first_name)



