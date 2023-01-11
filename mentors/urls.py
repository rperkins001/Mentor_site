from django.urls import path
from . import views

urlpatterns = [

    path('request_mentorship/', views.request_mentorship, name='request_mentorship'),
    path('request_success/', views.request_success, name='request_success'),
    
    #Admin?
    path('pending_mentor_requests/', views.pending_mentor_requests, name='pending_mentor_requests'),
    path('approve_mentor_request/', views.approve_mentor_request, name='approve_mentor_request'),
    path('reject_mentor_request/', views.reject_mentor_request, name='reject_mentor_request'),
    
    #path('search_mentor_listings/', views.search_mentor_listings, name='search_mentor_listings'),
    #path('search_results/', views.search_results, name='search_results'),
    path('search_view/', views.search_view, name='search_view'),
    path('no_results_found_view/', views.no_results_found_view, name='no_results_found_view'),

    path('mentor_search/', views.mentor_search, name='mentor_search'),
    path('mentor_profile/', views.mentor_profile, name='mentor_profile'),
    path('mentor/<int:mentor_id>/', views.mentor_details, name='mentor_details'),
    path('create_mentor_listing/', views.create_mentor_listing, name='create_mentor_listing'),

    path('previous_offers/', views.previous_offers, name='previous_offers'),
  
    
    
    
]

