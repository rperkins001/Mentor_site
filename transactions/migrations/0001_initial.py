# Generated by Django 3.2.9 on 2023-01-09 02:28

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0006_auto_20230109_0223'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True, verbose_name='Order ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Date Created')),
                ('quantity', models.DecimalField(decimal_places=0, max_digits=2, verbose_name='Quantity')),
                ('pricePer', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Price per Unit')),
                ('totalPaid', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total Paid')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_placed_by', to='users.profile')),
                ('mentor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_received_by', to='users.profile')),
            ],
        ),
    ]
