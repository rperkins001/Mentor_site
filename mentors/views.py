from .forms import MentorRequestForm, MentorListingForm, MentorListingSearchForm
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .utils import compute_score, rank_results
from .models import Mentor, Offer
from users.models import Profile
from django.db.models import Q



def request_mentorship(request):
    if request.method == 'POST':
        form = MentorRequestForm(request.POST)
        if form.is_valid():
            # Get the user's profile
            profile = request.users.profile
            # Set the is_mentor_requested field to True ????????????????
            profile.is_mentor_requested = True
            # Save the user's profile
            profile.save()
            return redirect('mentors:request_success')
    else:
        form = MentorRequestForm()
    return render(request, 'mentors/request.html', {'form': form})

def request_success(request):
    return render(request, 'mentors/request_success.html')

def pending_mentor_requests(request):
    # Get all user profiles with is_mentor_requested set to True
    mentor_requests = Profile.objects.filter(is_mentor_requested=True)
    return render(request, 'mentors/pending_requests.html', {'mentor_requests': mentor_requests})

def approve_mentor_request(request, request_id):
    # Get the user profile for the requested mentor request
    request = get_object_or_404(Profile, id=request_id, is_mentor_requested=True)
    # Set the is_mentor field to True
    request.is_mentor = True
    # Save the user profile
    request.save()
    return redirect('mentors:pending_requests')

def reject_mentor_request(request, request_id):
    # Get the user profile for the requested mentor request
    request = get_object_or_404(Profile, id=request_id, is_mentor_requested=True)
    # Set the is_mentor_requested field to False
    request.is_mentor_requested = False
    # Save the user profile
    request.save()
    return redirect('mentors:pending_requests')


'''
def search_mentor_listings(request):
    if request.method == 'POST':
        form = MentorListingSearchForm(request.POST)
        if form.is_valid():
            keywords = form.cleaned_data['keywords']
            areas_of_expertise = form.cleaned_data['areas_of_expertise']
            # Query the database for mentor listings that match the search criteria
            mentor_listings = Mentor.objects.filter(
                keywords__contains=keywords,
                areas_of_expertise__contains=areas_of_expertise
            ).order_by('-created_at')
            return render(request, 'mentors/search_results.html', {'mentor_listings': mentor_listings})
    else:
        form = MentorListingSearchForm()
    return render(request, 'mentors/search_mentor_listings.html', {'form': form})'''


def search_view(request):
    query = request.GET.get('q')  # Get the search query from the request
    if query:  # Check if a query was submitted
        results = Mentor.objects.filter(
            Q(first_name__contains=query) |
            Q(last_name__contains=query) |
            Q(company__contains=query) |
            Q(industry__contains=query)
        )
        ranked_results = rank_results(results, query)  # Rank the results by relevance
        return render(request, 'mentors/search_results.html', {'query': query, 'results': ranked_results})
    return redirect('homepage')  # Redirect to the homepage if no query was submitted

def no_results_found_view(request):
    return render(request, 'mentors/no_results_found.html')

'''
def search_view(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        results = Profile.objects.filter(name__contains=query)
        ranked_results = rank_results(results, query)
        if ranked_results:
            return render(request, 'users/search_results.html', {'query': query, 'results': ranked_results})
        else:
            return redirect('no_results_found')
    #return render(request, 'users/search.html', {'form': form})'''

from django.shortcuts import render
from .forms import MentorSearchForm

def mentor_search_view(request):
    form = MentorSearchForm()
    return render(request, 'mentors/mentor_search.html', {'form': form})



def mentor_search(request):
    mentors = Mentor.objects.all()
    industry = request.GET.get('industry')
    if industry:
        mentors = mentors.filter(industry__icontains=industry)
    return render(request, 'mentors/mentor_search.html', {'mentors': mentors})

def mentor_profile(request, mentor_id):
    mentor = get_object_or_404(Mentor, pk=mentor_id)
    timeslots = mentor.timeslot_set.all()
    offers = mentor.offer_set.all()
    reviews = mentor.review_set.all()
    context = {'mentor': mentor, 'timeslots': timeslots, 'offers': offers, 'reviews': reviews}
    return render(request, 'mentors/mentor_profile.html', context)

def mentor_details(request, mentor_id):
    mentor = Mentor.objects.get(id=mentor_id)
    context = {'mentor': mentor}
    return render(request, 'mentor_details.html', context)

def create_mentor_listing(request):
    if request.method == 'POST':
        form = MentorListingForm(request.POST)
        if form.is_valid():
            # Create a new Mentor object and save it to the database
            mentor = Mentor()
            mentor.areas_of_expertise = form.cleaned_data['areas_of_expertise']
            mentor.types_of_mentorship = form.cleaned_data['types_of_mentorship']
            mentor.availability = form.cleaned_data['availability']
            mentor.price = form.cleaned_data['price']
            # Associate the mentor with the current user's profile
            mentor.profile = request.user.profile
            mentor.save()
            return redirect('mentors:mentor_listing_success')
    else:
        form = MentorListingForm()
    return render(request, 'mentors/create_mentor_listing.html', {'form': form})


def previous_offers(request):
    time_slots = {}
    return render(request, 'mentors/previous_offers.html', {'time_slots': time_slots})


