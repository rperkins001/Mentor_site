from django.db import models
import uuid
from django.db.models.deletion import CASCADE
from users.models import Profile

class Mentor(Profile):
    industry = models.CharField(max_length=200, blank=True, null=True)
    company = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return f'{self.user.first_name} {self.user.last_name}'
    
TYPE_CHOICES = [
    ('option1', 'Option 1'),
    ('option2', 'Option 2'),
    ('option3', 'Option 3'),
    ('option4', 'Option 4'),
]

STATUS_CHOICES = [
    ('active', 'Active'),
    ('inactive', 'Inactive'),
]

class Offer(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50, choices=TYPE_CHOICES)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    mentor = models.ForeignKey(Mentor, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)
    description = models.TextField(blank=True, null=True)
    units_available = models.PositiveIntegerField(default=1)
    status = models.CharField(max_length=50, default='active', choices=STATUS_CHOICES)
    
    def __str__(self):
        return str(self.mentor)
    
    
    



