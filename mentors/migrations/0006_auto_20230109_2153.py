# Generated by Django 3.2.9 on 2023-01-09 21:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0005_delete_order'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mentor',
            name='company',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='mentor',
            name='industry',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
