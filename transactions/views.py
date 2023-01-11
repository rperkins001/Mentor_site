from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.templatetags.static import static
from mentors.models import Offer
from django.db.models import Q
import stripe
import tweepy
import os

def add_to_cart(request, mentor_id):
    if request.method == 'POST':
        offer_id = request.POST['offer']
        offer = Offer.objects.get(id=offer_id)
        cart = request.session.get('cart', [])
        cart.append(offer_id)
        request.session['cart'] = cart
    return redirect('mentor_details', mentor_id=mentor_id)

def cart(request):
    cart = request.session.get('cart', [])
    context = {'cart': cart}
    return render(request, 'cart.html', context)

stripe.api_key = "YOUR_STRIPE_SECRET_KEY"

def checkout(request):
    if request.method == 'POST':
        email = request.POST['email']
        credit_card_number = request.POST['credit_card_number']

        # Create a Stripe Customer
        customer = stripe.Customer.create(
            email=email,
            source=credit_card_number,
        )

        # Calculate the total amount to charge
        cart = request.session.get('cart', [])
        total_amount = 0
        for offer_id in cart:
            offer = Offer.objects.get(id=offer_id)
            total_amount += offer.price

        # Create a Stripe Charge
        charge = stripe.Charge.create(
            customer=customer.id,
            amount=total_amount * 100,  # Convert to cents
            currency='usd',
            description='Mentorship purchase',
        )

        # Check if the charge was successful
        if charge.status == 'succeeded':
            # Clear the cart
            del request.session['cart']
            return render(request, 'mentors/checkout_success.html')
        else:
            return render(request, 'mentors/checkout_failure.html')

#@login_required
def purchase_confirmation(request, pk):
    #time_slot = TimeSlot.objects.get(pk=pk)
    return render(request, 'users/purchase_confirmation.html') #{'time_slot': time_slot})

def purchase_success(request):
    return render(request, 'users/purchase_success.html')

#@login_required
def purchase_history(request):
    #time_slots = MentorTimeSlot.objects.filter(user=request.user)
    return render(request, 'users/purchase_history.html')#, {'time_slots': time_slots})


