from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django import forms
from .models import *  



class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'email', 'username', 'password1', 'password2']
        labels = {
            'first_name': 'Name',
        }

    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})


class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'username',
                  'location', 'bio', 'short_intro', 'profile_image',
                  'social_github', 'social_linkedin', 'social_twitter',
                  'social_youtube', 'social_website']

    def __init__(self, *args, **kwargs):
        super(ProfileForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs.update({'class': 'input'})
            
class MentorRequestForm(forms.Form):
    areas_of_expertise = forms.CharField(max_length=500)
    coaching_experience = forms.CharField(max_length=500)

class CreateOfferForm(forms.Form):
    TYPE_CHOICES = [
        ('option1', 'Option 1'),
        ('option2', 'Option 2'),
        ('option3', 'Option 3'),
        ('option4', 'Option 4'),
        ('option5', 'Option 5'),
        ('option6', 'Option 6'),
    ]
    type = forms.ChoiceField(choices=TYPE_CHOICES, widget=forms.RadioSelect)
    bio = forms.CharField(widget=forms.Textarea)
    price = forms.DecimalField(max_digits=10, decimal_places=2)
    active_status = forms.BooleanField(required=True)


class Post_your_passion(ModelForm):
    pass

class SignupForm(forms.Form):
    first_name = forms.CharField(max_length=255)
    last_name = forms.CharField(max_length=255)
    email = forms.EmailField()
    username = forms.CharField(max_length=255)
    password = forms.CharField(widget=forms.PasswordInput)
    

class CustomLoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if not username:
            raise forms.ValidationError('Please enter a username')
        if not password:
            raise forms.ValidationError('Please enter a password')



class SearchForm(forms.Form):
    query = forms.CharField(label='Search')
    




