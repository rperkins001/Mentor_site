from django.contrib.auth import views as auth_views
from django.contrib.auth import login
from django.urls import path
from . import views

urlpatterns = [

    #path('', views.homepage, name='homepage'),

    path('contact_view/', views.contact_view, name='contact_view'),
    path('contact_success_view/', views.contact_success_view, name='contact_success_view'),
    
    path('sitemap/', views.sitemap, name='sitemap'),
    path('about-us/', views.about_us, name='about_us'),
    path('site-policy/', views.site_policy, name='site_policy'),
    path('arbitration/', views.arbitration, name='arbitration'),
    path('financial_FAQs/', views.financial_FAQs, name='financial_FAQs'),
    
    path('media_feed/', views.media_feed, name='media_feed'),
    path('public_pitches/', views.public_pitches, name='public_pitches'),

    path('employment_portal/', views.employment_portal, name='employment_portal'),
    path('job_listings/', views.job_listings, name='job_listings'),
    path('job_detail/', views.job_detail, name='job_detail'),
    path('apply_for_job/', views.apply_for_job, name='apply_for_job'),

    ]