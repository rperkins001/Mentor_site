# Generated by Django 3.2.9 on 2023-01-08 15:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mentors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='mentor',
            old_name='areas_of_expertise',
            new_name='company',
        ),
        migrations.RenameField(
            model_name='mentor',
            old_name='coaching_experience',
            new_name='industry',
        ),
    ]
