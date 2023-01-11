from django.shortcuts import render, redirect, get_object_or_404
from django.templatetags.static import static
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.forms.widgets import PasswordInput
from django.contrib.auth.models import User
from .models import Tweet
from mentors.models import Mentor
from users.models import Profile
from django.db.models import Q
import tweepy
import os
from .utils import compute_score, rank_results

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail

from .forms import ResumeForm, JobApplicationForm
from .models import Resume, Job, JobPosting, JobApplication

def contact_view(request):
    if request.method == 'POST':
        # Get the form data
        name = request.POST['name']
        email = request.POST['email']
        message = request.POST['message']
        
        # Send the message
        send_mail(
            'Contact Form Message',
            message,
            email,
            ['admin@example.com'],
            fail_silently=False,
        )
        
        return render(request, 'public/contact_success.html')
    else:
        # Render the contact form template
        return render(request, 'public/contact.html')

def contact_success_view(request):
    return render(request, 'public/contact_success.html')


def sitemap(request):
    pages = [
        {'title': 'Homepage', 'url': '/'},
        {'title': 'Site Policy', 'url': '/site-policy/'},
        {'title': 'About Us', 'url': '/about-us/'},
        {'title': 'Contact Us', 'url': '/contact-us/'},
        {'title': 'Login', 'url': '/login/'},
        {'title': 'User Profile', 'url': '/user-profile/'},
        {'title': 'Profile Settings', 'url': '/profile-settings/'},
        {'title': 'Purchase Confirmation', 'url': '/purchase-confirmation/'},
        {'title': 'Purchase Success', 'url': '/purchase-success/'},
        {'title': 'Purchase History', 'url': '/purchase-history/'},
    ]
    return render(request, 'public/sitemap.html', {'pages': pages})

def about_us(request):
    context={}
    return render(request, 'public/about_us.html', context)

def site_policy(request):
    return render(request, 'public/site_policy.html')


def arbitration(request):
    return render(request, 'public/arbitration.html')

def financial_FAQs(request):
    faqs = [
        {
            "question": "What types of payment do you accept?",
            "answer": "We accept Visa, Mastercard, and American Express.",
        },
        {
            "question": "Is my personal information safe?",
            "answer": "We take the security of our customers' personal information very seriously. All transactions are processed using secure servers and encrypted data transmission.",
        },
        {
            "question": "What is your refund policy?",
            "answer": "We offer a full refund for any orders that are cancelled within 24 hours of purchase. After that time, we are unable to offer a refund.",
        },
    ]
    return render(request, "public/financial_faqs.html", {"faqs": faqs})


def media_feed(request):
    # Set up authentication
    #auth = tweepy.OAuth1UserHandler(
    #    consumer_key,
    #    consumer_secret,
    #    access_token,
    #    access_token_secret
    #    )
    #api = tweepy.API(auth)

    # Retrieve the latest tweets from the user's timeline
    #tweets = api.user_timeline()

    # Print the text of the tweets
    #for tweet in tweets:
    #    print(tweet.text)

    tweets = Tweet.objects.all()
    return render(request, 'public/media_feed.html', {'tweets': tweets})

    # Use the tweepy library to authenticate and access the Twitter API
    #api = tweepy.API(auth)

    # Retrieve the tweets from your Twitter accounts
    #tweets = api.user_timeline(screen_name='your_twitter_handle')

    # Render the tweets on the live feed page
    #return render(request, 'live_feed.html', {'tweets': tweets})

def public_pitches(request):
    # Retrieve a list of passion projects from the database
    projects = 1#PassionProject.objects.all()
    return render(request, 'public/public_pitches.html', {'projects': projects})
# Passion Gallery
#def client_side_PostYourPassion(request):


def employment_portal(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('resume_submitted')
    else:
        form = ResumeForm()
    jobs = Job.objects.all()
    return render(request, 'public/employment_portal.html', {'jobs': jobs, 'form': form})

def job_listings(request):
    job_listings = JobPosting.objects.all()
    return render(request, 'public/job_listings.html', {'job_listings': job_listings})

def job_detail(request, job_id):
    # Get the details for a specific job posting
    job = get_object_or_404(Job, pk=job_id)
    return render(request, 'public/job_detail.html', {'job': job})

def apply_for_job(request, job_id):
    job = get_object_or_404(JobPosting, pk=job_id)
    if request.method == 'POST':
        form = JobApplicationForm(request.POST)
        if form.is_valid():
            application = form.save(commit=False)
            application.job = job
            application.user = request.user
            application.save()
            return redirect('application_submitted')
    else:
        form = JobApplicationForm()
    return render(request, 'public/apply_for_job.html', {'form': form, 'job': job})    


    





