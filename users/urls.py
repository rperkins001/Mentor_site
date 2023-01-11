from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.contrib.auth import login
from django.conf import settings
from django.urls import path
from . import views

urlpatterns = [

    path('', views.homepage, name='homepage'),
    path('signup/', views.signup, name='signup'),
    path('signup-success/', views.signup_success, name='signup_success'),
    path('forgot-password', views.ForgotPasswordView, name='forgot_password'),
    path('password_reset_done/', views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('profile-settings/<int:id>/', views.profile_settings, name='profile_settings'),
    path('profile/<int:id>/', views.user_profile, name='user_profile'),
    
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)