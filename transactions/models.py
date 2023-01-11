from django.db import models
from users.models import Profile
from django.db import models
import uuid
from django.db.models.deletion import CASCADE

# Create your models here.

class Order(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False, verbose_name='Order ID')
    created = models.DateTimeField(auto_now_add=True, verbose_name='Date Created')
    client = models.ForeignKey(Profile, related_name='order_placed_by', on_delete=models.CASCADE)
    mentor = models.ForeignKey(Profile, related_name='order_received_by', on_delete=models.CASCADE)
    quantity = models.DecimalField(max_digits=2, decimal_places=0, verbose_name='Quantity')
    pricePer = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Price per Unit')
    totalPaid = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total Paid')

    def __str__(self):
        return f'Order {self.id} for {self.quantity} units at {self.pricePer} each (total: {self.totalPaid})'
