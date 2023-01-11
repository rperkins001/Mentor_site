from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.tokens import default_token_generator
from django.utils.http import urlsafe_base64_encode
from django.templatetags.static import static
from django.utils.encoding import force_bytes
from django.core.mail import send_mail
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from .forms import SignupForm, CustomLoginForm
from django.contrib.auth.forms import PasswordResetForm
from django.contrib.auth.views import PasswordResetDoneView
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.core.mail import send_mail
from mentors.models import Mentor
from users.models import Profile
from .forms import ProfileForm, SignupForm, CustomLoginForm
from django.db.models import Q
import os


def homepage(request):
    # Get the list of image files in the images directory
    image_list = os.listdir('static/css/images')

    # Remove any non-image files from the list
    image_list = [f for f in image_list if f.endswith(('.jpg', '.png', '.gif'))]

    # Prepend the file path to each image file in the list
    image_list = ['images/' + f for f in image_list]

    return render(request, 'users/homepage.html', {'image_list': image_list})

def photo_grid_view(request):
    # Get the list of image files in the images directory
    image_list = os.listdir('static/css/images')

    # Remove any non-image files from the list
    image_list = [f for f in image_list if f.endswith(('.jpg', '.png', '.gif'))]

    # Prepend the file path to each image file in the list
    image_list = ['static/css/images/' + f for f in image_list]

    return render(request, 'users/photo_grid.html', {'photos': image_list})

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            email = form.cleaned_data['email']
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            profile = Profile(first_name=first_name, last_name=last_name, email=email, username=username)
            user = User.objects.create_user(username=username, password=password, email=email, first_name=first_name, last_name=last_name)
            user.save()
            profile.user = user
            profile.save()
            
            #send_mail(
            #    'Welcome to Our Site!',
            #    'Thank you for signing up. We hope you enjoy using our site!',
            #    'noreply@example.com',
            #    [form.cleaned_data['email']],
            #    fail_silently=False,
            #)
            return redirect('signup_success')
        else:
            print("Form is not valid!")
    else:
        form = SignupForm()
    return render(request, 'users/signup.html', {'form': form})

def signup_success(request):
    return render(request, 'users/signup_success.html')


def login_view(request):
    if request.method == 'POST':
        form = CustomLoginForm(request.POST)
        if form.is_valid():
            # Authenticate the user and log them in
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                # Get the user's profile and redirect to the user profile view with the user's id
                profile = Profile.objects.get(user=user)
                return redirect('user_profile', id=user.id)
            else:
                # Display an error message if the authentication failed
                print('user is none. sorry.')
                form.add_error(None, 'Invalid username or password')
        else:
            print("Form is not valid!")
    else:
        # Render the login form if the request is a GET request
        form = CustomLoginForm()
    return render(request, 'registration/login.html', {'form': form, 'signup_url': 'signup', 'forgot_password_url': 'forgot_password'})

def logout_view(request):
    # Log the user out
    logout(request)
    # Redirect the user to the homepage
    return redirect('homepage')

class ForgotPasswordView(FormView):
    form_class = PasswordResetForm
    template_name = 'registration/forgot_password.html'
    success_url = reverse_lazy('password_reset_done')
    
    def form_valid(self, form):
        # Send the password reset email
        opts = {
            'use_https': self.request.is_secure(),
            'token_generator': default_token_generator,
            'from_email': 'webmaster@example.com',
            'request': self.request,
        }
        form.save(**opts)
        return super().form_valid(form)
    
class PasswordResetDoneView(PasswordResetDoneView):
    template_name = 'registration/password_reset_done.html'
    
def user_profile(request, id):
    # Retrieve the currently logged in user
    current_user = request.user
    # Retrieve the user whose profile is being viewed
    try:
        user = User.objects.get(id=id)
    except User.DoesNotExist:
        return HttpResponse("User not found", status=404)
    # Retrieve the profile for the user being viewed
    profile = user.profile
    #activities =  # code to retrieve the recent activity of the user
    context = {
        'profile': profile,
        'user': user,
        'user_id': id,
        #'activities': activities,
    }
    # Render the profile template with the profile information
    return render(request, 'users/user_profile.html', context)

#@login_required
def profile_settings(request, id):
    user = User.objects.get(pk=id)
    profile = user.profile
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            # Save the uploaded photo
            profile_photo = form.cleaned_data['profile_photo']
            profile.profile_photo = profile_photo
            profile.save()
            return redirect('user_profile')
        
    else:
        form = ProfileForm()
    return render(request, 'users/profile_settings.html', {'form': form, 'user_id': id})