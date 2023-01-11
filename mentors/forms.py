from django import forms

class MentorRequestForm(forms.Form):
    # A text field for the user to provide information about why they want to become a mentor
    reason_for_request = forms.CharField(widget=forms.Textarea)
    # A text field for the user to provide information about their qualifications and experience as a mentor
    qualifications = forms.CharField(widget=forms.Textarea)

class MentorListingForm(forms.Form):
    # Fields for the mentor to specify details about their mentorship offering go here
    areas_of_expertise = forms.CharField(max_length=200)
    types_of_mentorship = forms.CharField(max_length=200)
    availability = forms.CharField(max_length=200)
    # Add a field for the price of the mentorship offering
    price = forms.DecimalField(max_digits=6, decimal_places=2)
    # You can add additional fields as needed

class MentorListingSearchForm(forms.Form):
    keywords = forms.CharField(required=False)
    areas_of_expertise = forms.CharField(required=False)
    

class MentorSearchForm(forms.Form):
    INDUSTRY_CHOICES = [
        ('Technology', 'Technology'),
        ('Finance', 'Finance'),
        ('Marketing', 'Marketing'),
        # Add more choices here
    ]
    industry = forms.MultipleChoiceField(choices=INDUSTRY_CHOICES, required=False)
    location = forms.CharField(max_length=200, required=False)
    